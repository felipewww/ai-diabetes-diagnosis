import numpy as np
import pandas as pd

def zero_to_mean(df: pd.DataFrame):
    non_zero_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    df[non_zero_cols] = df[non_zero_cols].replace(0, np.nan)

    for col in non_zero_cols:
        df[col] = df[col].fillna(df[col].mean())

def zero_to_nan(X):
    X = X.copy()
    X[X == 0] = np.nan
    return X

# def zero_to_nan(df: pd.DataFrame):
#     # Crie uma cópia para evitar modificar o DataFrame original
#     df_copy = df.copy()
#     non_zero_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
#     df_copy[non_zero_cols] = df_copy[non_zero_cols].replace(0, np.nan)
#     return df_copy