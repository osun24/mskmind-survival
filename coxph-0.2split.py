import pandas as pd
from lifelines import CoxPHFitter
from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

def run_model(df, name):
    # Train-test split
    # Split the data into training and testing sets
    test_size = 0.2
    # Split the data into training and testing sets
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # Fit the Cox proportional hazards model on the training set
    cph = CoxPHFitter()
    cph.fit(train_df, duration_col='PFS_MONTHS', event_col='PFS_STATUS')

    # Print summary of the fitted model
    cph.print_summary(style="ascii")

    # Optional: Evaluate the model using the test set
    # For example, you can use the model's concordance index on the test set
    c_index = cph.concordance_index_
    print(f"Concordance Index on Training Set: {c_index:.3f}")

    # Evaluate the model on the test set
    c_index_test = cph.score(test_df, scoring_method="concordance_index")
    print(f"Concordance Index on Test Set: {c_index_test:.3f}")

    summary_df = cph.summary  # Get the summary as a DataFrame
    model_metrics = [cph.log_likelihood_, cph.concordance_index_]

    # Add a column for significance level
    def significance_stars(p):
        if p < 0.001:
            return "***"
        elif p < 0.01:
            return "**"
        elif p < 0.05:
            return "*"
        else:
            return ""

    summary_df['significance'] = summary_df['p'].apply(significance_stars)

    print(summary_df)

    concordance = cph.concordance_index_
    partial_aic = cph.AIC_partial_
    log_likelihood_ratio_test = cph.log_likelihood_ratio_test().test_statistic
    ll_ratio_test_df = cph.log_likelihood_ratio_test().degrees_freedom
    neg_log2_p_ll_ratio_test = -np.log2(cph.log_likelihood_ratio_test().p_value)

    with open(f'cph-{concordance:.2f}-{name}-summary.txt', 'w') as f:
        f.write(summary_df.to_string())
        formatted_metrics = '\n'.join([f'{metric:.4f}' for metric in model_metrics])
        f.write(f"\n\nModel metrics: {formatted_metrics}")
        
        # Write additional metrics in the specified format
        f.write(f"\n\nConcordance = {concordance:.2f}")
        f.write(f"\nPartial AIC = {partial_aic:.2f}")
        f.write(f"\nlog-likelihood ratio test = {log_likelihood_ratio_test:.2f} on {ll_ratio_test_df} df")
        f.write(f"\n-log2(p) of ll-ratio test = {neg_log2_p_ll_ratio_test:.2f}")
    # Extract the hazard ratios, confidence intervals, and p-values
    hazard_ratios = np.exp(cph.params_)  # Exponentiate the coefficients to get hazard ratios
    confidence_intervals = np.exp(cph.confidence_intervals_)  # Exponentiate confidence intervals
    p_values = cph.summary['p']  # Extract p-values from the summary

    # Plotting the forest plot
    plt.figure(figsize=(12, 8))

    # Include lambda value in the title 
    plt.title(f'{name} Hazard Ratios (Test Size: {test_size}, C-index: {c_index:.3f}, 95% CI)')

    # Generate a forest plot for hazard ratios with 95% confidence intervals
    plt.errorbar(hazard_ratios, range(len(hazard_ratios)), 
                xerr=[hazard_ratios - confidence_intervals.iloc[:, 0], confidence_intervals.iloc[:, 1] - hazard_ratios],
                fmt='o', color='black', ecolor='grey', capsize=5)

    # Add labels for the covariates
    plt.yticks(range(len(hazard_ratios)), cph.params_.index)
    plt.axvline(x=1, linestyle='--', color='red')  # Reference line at HR=1
    plt.xlabel('Hazard Ratio (log scale)')
    plt.xscale('log')  # Logarithmic scale for the hazard ratios

    x_pos = max(hazard_ratios) * 1.4  # Position the p-values far to the right
    for i, p in enumerate(p_values):
        if p < 0.05:
            plt.text(x_pos, i, f'$\\mathbf{{p={p:.3f}}}$', va='center', ha='left', fontsize=8)
        else:
            plt.text(x_pos, i, f'p={p:.3f}', va='center', ha='left', fontsize=8)

    # Adjust x-axis limits to ensure p-values are visible
    plt.xlim(left=min(hazard_ratios) / 2, right=x_pos * 1.15)

    # Display the plot
    plt.tight_layout()
    name = name.replace(' ', '-')
    plt.savefig(f'cph-{c_index:.2f}-{name}-forest-plot.png')
    plt.show()

# Without treatment data
surv = pd.read_csv('survival.csv')

parameters = ["IMPACT_TMB_SCORE", "CLINICALLY_REPORTED_PD-L1_SCORE", "ALBUMIN", "DNLR", "FRACTION_GENOME_ALTERED", "EGFR_DRIVER","STK11_DRIVER"]

# some unknown, some NA, some cigars
surv.drop(columns= ["PACK-YEAR_HISTORY"], inplace=True)

surv = surv[parameters + ['PFS_MONTHS', 'PFS_STATUS']]

# Drop those with low variance
run_model(surv, 'MSK MIND LUAD - RSF Selected Parameters')