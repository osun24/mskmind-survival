import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from lifelines import KaplanMeierFitter

# Read the data from CSV
df = pd.read_csv('survival.csv')

# Exclude specified variables
exclude_vars = [
    "CURRENT_SMOKER", "FORMER_SMOKER", "NEVER_SMOKER",
    "MET_DRIVER", "BRAF_DRIVER", "ARID1A_DRIVER"
]
df = df.drop(columns=exclude_vars)

print(df.columns)

# Select variables to plot

# 'PFS_STATUS', include PFS via KM
demographic_variables = ['AGE', 'IS_FEMALE', 'PACK-YEAR_HISTORY']
clinical_variables = ['ECOG', 'DNLR', 'ALBUMIN']
genomic_variables = ['EGFR_DRIVER', 'ERBB2_DRIVER', 'STK11_DRIVER', "IMPACT_TMB_SCORE", "CLINICALLY_REPORTED_PD-L1_SCORE", 'FRACTION_GENOME_ALTERED']
drug_variables = ['PEMBROLIZUMAB', 'ATEZOLIZUMAB', 'NIVOLUMAB']

def make_plots(variables_to_plot, name):
    # Determine grid size for subplots based on the number of variables
    n_plots = len(variables_to_plot)
    if n_plots == 3:
        n_rows = 1
        n_cols = 3
    elif n_plots == 4:
        n_rows = 1
        n_cols = 4
    elif n_plots == 6:
        n_rows = 2
        n_cols = 3
    else:
        n_cols = math.ceil(math.sqrt(n_plots))
        n_rows = math.ceil(n_plots / n_cols)

    # Create subplots with dynamic grid size
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))

    # Flatten axes array for easy indexing
    if n_plots == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    # Plotting loop
    for i, col in enumerate(variables_to_plot):
        ax = axes[i]
        if col == 'IS_FEMALE':
            # Pie chart
            counts = df[col].value_counts()
            labels = ['Male', 'Female'] if set(df[col]) == {0, 1} else counts.index
            ax.pie(counts, labels=labels, autopct='%1.1f%%')
            ax.set_title('Pie Chart of IS_FEMALE')
        elif col == 'PFS_MONTHS':
            # Kaplan-Meier Survival Curve
            T = df['PFS_MONTHS']
            E = df['PFS_STATUS']

            # Ensure E contains binary values 0 (censored) and 1 (event)
            # If PFS_STATUS is already in 0 and 1, this step may not be necessary
            E = E.replace({'0:LIVING': 0, '1:DECEASED': 1})

            kmf = KaplanMeierFitter()

            # Fit the data
            kmf.fit(T, event_observed=E, label='PFS')

            # Plot the Kaplan-Meier curve
            kmf.plot_survival_function(ax=ax, ci_show=True)
            ax.set_title('Kaplan-Meier Curve for PFS_MONTHS')
            ax.set_xlabel('Time (Months)')
            ax.set_ylabel('Survival Probability')
            ax.grid(True)
        else:
            n_unique = df[col].nunique()
            dtype = df[col].dtype
            if dtype == 'object' or n_unique <= 5:
                # Categorical or binary variable
                sns.countplot(x=col, data=df, ax=ax)
                ax.set_title(f'Count Plot of {col}')
                ax.set_xlabel(col)
                ax.set_ylabel('Count')
                
                # if binary, use orange bars for the affirmative
                if n_unique == 2:
                    ax.patches[1].set_facecolor('orange')
            else:
                # Quantitative variable
                sns.histplot(df[col].dropna(), kde=False, ax=ax)
                ax.set_title(f'Histogram of {col}')
                ax.set_xlabel(col)
                ax.set_ylabel('Frequency')

    # adjust spacing between plots
    plt.subplots_adjust(wspace=0, hspace=0)
    
    # Hide any unused subplots
    for j in range(i + 1, n_rows * n_cols):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig(f'{name}.png')
    plt.show()
    
def info():
    # Median PFS:
    print(f"Minimum PFS_MONTHS: {df['PFS_MONTHS'].min()}, Median PFS_MONTHS: {df['PFS_MONTHS'].median()}, Maximum PFS_MONTHS: {df['PFS_MONTHS'].max()}")
    
    # Number of patients with PFS_STATUS == 1
    print("Number of patients with PFS_STATUS == 1:", df['PFS_STATUS'].sum())
    print("Number of patients with PFS_STATUS == 0:", df.shape[0] - df['PFS_STATUS'].sum())
    
    # Age
    print(f"Minimum Age: {df['AGE'].min()}, Median Age: {df['AGE'].median()}, Maximum Age: {df['AGE'].max()}")
    
    # Pack-year
    print(f"Minimum Pack-Year History: {df['PACK-YEAR_HISTORY'].min()}, Median Pack-Year History: {df['PACK-YEAR_HISTORY'].median()}, Maximum Pack-Year History: {df['PACK-YEAR_HISTORY'].max()}")
    
#make_plots(demographic_variables, "EDA Demographic Plots - MSKMIND")
#make_plots(clinical_variables, "EDA Clinical Plots - MSKMIND")
#make_plots(genomic_variables, "eda/EDA Genomic Plots - MSKMIND")
make_plots(drug_variables, "eda/EDA Drug Plots - MSKMIND")