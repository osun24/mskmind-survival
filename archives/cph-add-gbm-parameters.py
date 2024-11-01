import pandas as pd
from lifelines import CoxPHFitter
from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

def dataframe_to_latex(df, caption="Table Caption", label="table:label"):
    """
    Convert a pandas DataFrame to a LaTeX tabular environment and print it.
    
    Parameters:
    - df: pandas DataFrame
    - caption: The caption of the table (optional)
    - label: The label for referencing the table in LaTeX (optional)
    """
    # Start the LaTeX table environment
    latex_str = "\\begin{table}[H]\n"
    latex_str += "\\centering\n"
    latex_str += f"\\caption{{{caption}}}\n"
    latex_str += f"\\label{{{label}}}\n"
    # afterwards do l c c for left on covariates
    latex_str += "\\begin{tabular}{" + " | ".join(['c' for _ in df.columns]) + "}\n"
    latex_str += "\\hline\n"

    # Add column headers
    latex_str += " & ".join(df.columns) + " \\\\\n"
    latex_str += "\\hline\n"

    # Make row values title case but keep driver names in all caps, like keep EGFR Driver
    df['Covariate'] = df['Covariate'].str.title()
    
    for i in range(len(df)):
        if 'Driver' in df['Covariate'][i]:
            driverName = df['Covariate'][i].split(' ')[0].upper()
            df['Covariate'][i] = driverName + ' Driver'
        
    # Add table rows
    for _, row in df.iterrows():
        # Bold p-values less than 0.05, \textbf{ $\leq$ 0.001 } for p-values less than 0.001
        if row['p'] < 0.001:
            row['p'] = f"\\textbf{{ $\leq$ 0.001 }}"
        elif row['p'] < 0.05:
            row['p'] = f"\\textbf{{{round(row['p'], 3)}}}"
        else: 
            row['p'] = round(row['p'], 3)
        latex_str += " & ".join(map(str, row.values)) + " \\\\\n"
        # latex_str += "\\hline\n"

    # End the LaTeX table environment
    latex_str += "\\end{tabular}\n"
    latex_str += "\\end{table}\n"

    # Print the LaTeX table
    print(latex_str)

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
    # cph.print_summary(style="ascii")

    # Optional: Evaluate the model using the test set
    # For example, you can use the model's concordance index on the test set
    c_index = cph.concordance_index_
    print(f"Concordance Index on Training Set: {c_index:.3f}")

    # Evaluate the model on the test set
    c_index_test = cph.score(test_df, scoring_method="concordance_index")
    print(f"Concordance Index on Test Set: {c_index_test:.3f}")
    return c_index_test


# Without treatment data
surv = pd.read_csv('survival.csv')

surv.drop(columns = ["PEMBROLIZUMAB", "ATEZOLIZUMAB", "NIVOLUMAB", "CURRENT_SMOKER", "FORMER_SMOKER", "NEVER_SMOKER"], inplace = True)

rankedParameters = ["ALBUMIN", "CLINICALLY_REPORTED_PD-L1_SCORE", "PACK-YEAR_HISTORY", "DNLR", "IMPACT_TMB_SCORE", "AGE", "FRACTION_GENOME_ALTERED", "ECOG", "EGFR_DRIVER", "ERBB2_DRIVER", "MSI_SCORE", "IS_FEMALE", "STK11_DRIVER"]

runningParameters = []
c_indicies = {}
for p in rankedParameters:
    print(p)
    runningParameters.append(p)
    surv_copy = surv[runningParameters + ['PFS_MONTHS', 'PFS_STATUS']].copy()
     
    c_indicies[p] = run_model(surv_copy, len(runningParameters))
    
# Plot c-indicies by inclusion of parameter
plt.figure(figsize = (12, 8))
plt.subplots_adjust(left=0.065, bottom=0.31, right=0.974, top=0.88)
plt.plot(c_indicies.keys(), c_indicies.values(), marker='o')
plt.xticks(rotation=45)
plt.xlabel('Parameters Included')
plt.ylabel('Concordance Index')
plt.title('Concordance Index by Inclusion of Parameters for GBM')
plt.grid()
plt.savefig('cph-c-index-over-gbm-parameters.png')
plt.show()
