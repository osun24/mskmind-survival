import pandas as pd
import numpy as np
from sksurv.ensemble import RandomSurvivalForest
from sksurv.util import Surv
from sksurv.metrics import concordance_index_censored
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
import joblib

def create_rsf(df, name, trees=1000):
    # Create structured array for survival analysis
    surv_data = Surv.from_dataframe('PFS_STATUS', 'PFS_MONTHS', df)
    
    covariates = df.columns.difference(['PFS_STATUS', 'PFS_MONTHS'])

    test_size = 0.2
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[covariates], surv_data, test_size=test_size, random_state=42)

    # Fit the Random Survival Forest model
    rsf = RandomSurvivalForest(n_estimators=trees, min_samples_split=10, min_samples_leaf=8, random_state=42)
    rsf.fit(X_train, y_train)

    # Evaluate model performance
    c_index = concordance_index_censored(y_test['PFS_STATUS'], y_test['PFS_MONTHS'], rsf.predict(X_test))
    print(f"C-index: {c_index[0]:.3f}")
    
    # Train c-index
    train_c_index = concordance_index_censored(y_train['PFS_STATUS'], y_train['PFS_MONTHS'], rsf.predict(X_train))
    print(f"Train C-index: {train_c_index[0]:.3f}")

    # Save the RSF model to a file
    joblib.dump(rsf, f'rsf_model-{trees}-c{c_index[0]:.3f}.pkl')

    result = permutation_importance(rsf, X_test, y_test, n_repeats=5, random_state=42)

    importances_df = pd.DataFrame({
        "importances_mean": result.importances_mean,
        "importances_std": result.importances_std
    }, index=X_test.columns).sort_values(by="importances_mean", ascending=False)

    print(importances_df)

    importances_df = importances_df.sort_values(by="importances_mean", ascending=True)  # Ascending for better barh plot

    # Plot the feature importances
    plt.figure(figsize=(20, 16))
    plt.barh(importances_df.index, importances_df["importances_mean"], xerr=importances_df["importances_std"], color='skyblue')
    plt.xlabel("Permutation Importance")
    plt.ylabel("Feature")
    plt.title(f"{name} Feature Importances: {trees} Trees, {test_size} Test Size, C-index: {c_index[0]:.3f}")
    plt.tight_layout()
    name = name.replace(' ', '-')
    plt.savefig(f'rsf-importances-{name}-{trees}trees-{test_size}testsize.png')
    plt.show()

# Without treatment data
surv = pd.read_csv('survival.csv')
surv.drop(columns = ["PACK-YEAR_HISTORY", "PEMBROLIZUMAB", "ATEZOLIZUMAB", "NIVOLUMAB"], inplace = True)

create_rsf(surv, 'MSK MIND LUAD', 250)