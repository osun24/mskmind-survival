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

# Load the dataset
df = pd.read_csv('survival.csv')

df.drop(columns = ["PACK-YEAR_HISTORY", "PEMBROLIZUMAB", "ATEZOLIZUMAB", "NIVOLUMAB"], inplace = True)

covariates = df.columns.difference(['PFS_STATUS', 'PFS_MONTHS'])

# Create structured array for survival analysis
surv_data = Surv.from_dataframe('PFS_STATUS', 'PFS_MONTHS', df)

test_size = 0.2
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[covariates], surv_data, test_size=test_size, random_state=42)

# Instantiate the model with desired hyperparameters
gbm = GradientBoostingSurvivalAnalysis(
    loss="coxph",
    learning_rate=0.1,
    n_estimators=80,
    subsample=1.0,
    random_state=42, 
    validation_fraction=0.1,
    n_iter_no_change=10
)

# Fit the model
gbm.fit(X_train, y_train)

# Predict the risk scores for the test set
risk_scores = gbm.predict(X_test)

c_index = concordance_index_censored(y_test['PFS_STATUS'], y_test['PFS_MONTHS'], risk_scores)
print(f"C-index: {c_index[0]:.3f}")

print(f"Train C-index: {concordance_index_censored(y_train['PFS_STATUS'], y_train['PFS_MONTHS'], gbm.predict(X_train))[0]:.3f}")

# implement cross-validation

joblib.dump(gbm, f'gbm_model-{gbm.n_estimators}-c{c_index[0]:.3f}.pkl')

# Get feature importances
importances = gbm.feature_importances_

# Create a DataFrame
importances_df = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

# Print the features that have non-zero importance as
print(importances_df[importances_df["Importance"] > 0])

# Print features with non-zero importance as a list
print(importances_df[importances_df["Importance"] > 0]["Feature"].tolist())

# Plot the feature importances
plt.figure(figsize=(12, 8))
plt.barh(importances_df["Feature"], importances_df["Importance"], color='skyblue')
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title(f"Feature Importances: {gbm.n_estimators} Estimators, Test Size: {test_size}, C-index: {c_index[0]:.3f}")
plt.gca().invert_yaxis()  # Highest importance at the top
plt.tight_layout()
plt.savefig(f'gbm-importances-{gbm.n_estimators}trees-{test_size}testsize.png')
plt.show()
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