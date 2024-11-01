import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

# Load data
surv = pd.read_csv('survival.csv')

# Drop columns with low variance
surv.drop(columns= ["PACK-YEAR_HISTORY", "ALBUMIN", "AGE"], inplace=True)

# Function to calculate VIF
def calculate_vif(df):
    vif_data = pd.DataFrame()
    vif_data["feature"] = df.columns
    vif_data["VIF"] = [variance_inflation_factor(df.values, i) for i in range(len(df.columns))]
    return vif_data

# Calculate VIF
vif_data = calculate_vif(surv.select_dtypes(include=[np.number]))
print(vif_data)

# Drop features with high VIF (e.g., VIF > 10)
high_vif_features = vif_data[vif_data["VIF"] > 10]["feature"]
print(f"High VIF features: {high_vif_features}")

corr_matrix = surv.corr()
print(corr_matrix)