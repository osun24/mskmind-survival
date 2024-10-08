import pandas as pd
import numpy as np
from sksurv.ensemble import RandomSurvivalForest
from sksurv.util import Surv
from sksurv.metrics import concordance_index_censored
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
from sksurv.metrics import concordance_index_censored
import joblib
from sksurv.ensemble import GradientBoostingSurvivalAnalysis
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

def run_gbm_trees(df, surv_data, covariates, name):
    n_estimators_list = np.linspace(10,1000,25, dtype=int)
    
    train_c_indices = []
    test_c_indices = []
    
    test_size = 0.2
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[covariates], surv_data, test_size=test_size, random_state=42)
    
    for n_estimators in n_estimators_list:
        # Instantiate the model with desired hyperparameters
        gbm = GradientBoostingSurvivalAnalysis(
            loss="coxph",
            learning_rate=0.1,
            n_estimators=n_estimators,
            subsample=1.0,
            random_state=42, 
            validation_fraction=0.1,
            n_iter_no_change=10
        )

        # Fit the model
        gbm.fit(X_train, y_train)

        # Evaluate model performance on the training set
        train_c_index = concordance_index_censored(y_train['PFS_STATUS'], y_train['PFS_MONTHS'], gbm.predict(X_train))
        train_c_indices.append(train_c_index[0])  # Store the training c-index
        
        # Evaluate model performance on the test set
        test_c_index = concordance_index_censored(y_test['PFS_STATUS'], y_test['PFS_MONTHS'], gbm.predict(X_test))
        test_c_indices.append(test_c_index[0])  # Store the test c-index
        
        print(f"Number of Trees: {n_estimators}, Test C-index: {test_c_index[0]:.3f}")
    
    # Plot Train and Test C-index with Confidence Intervals
    plt.figure(figsize=(10, 6))
    plt.plot(n_estimators_list, train_c_indices, label='Train C-index')
    plt.plot(n_estimators_list, test_c_indices, label='Test C-index')
    plt.xlabel('Number of Trees')
    plt.ylabel('C-index')
    plt.title(f'{name} Train and Test C-index with 95% CI vs Number of Trees - Test Size: {test_size}, Random State: 42')
    plt.legend()
    plt.grid()
    plt.savefig(f'gbm-{name}-numtrees-vs-c-testsize{test_size}-iters-state42.png')
    plt.show()

# Load the dataset
df = pd.read_csv('survival.csv')

df.drop(columns = ["PEMBROLIZUMAB", "ATEZOLIZUMAB", "NIVOLUMAB", "CURRENT_SMOKER", "FORMER_SMOKER", "NEVER_SMOKER"], inplace = True)

covariates = df.columns.difference(['PFS_STATUS', 'PFS_MONTHS'])

# Create structured array for survival analysis
surv_data = Surv.from_dataframe('PFS_STATUS', 'PFS_MONTHS', df)

run_gbm_trees(df, surv_data, covariates, 'MSK MIND LUAD')
        
"""
param_grid = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [100, 200, 500],
    'subsample': [0.5, 0.75, 1.0],
    'max_depth': [1, 3, 5]
}

gbm_cv = GradientBoostingSurvivalAnalysis(random_state=42)

grid_search = GridSearchCV(
    gbm_cv,
    param_grid,
    cv=5,
    scoring='neg_brier_score',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print(f"Best cross-validated C-index: {grid_search.best_score_:.3f}")"""