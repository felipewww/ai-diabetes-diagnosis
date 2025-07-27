import numpy as np
import pandas as pd

def zero_to_mean(df: pd.DataFrame):
    non_zero_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    df[non_zero_cols] = df[non_zero_cols].replace(0, np.nan)

    for col in non_zero_cols:
        df[col] = df[col].fillna(df[col].mean())