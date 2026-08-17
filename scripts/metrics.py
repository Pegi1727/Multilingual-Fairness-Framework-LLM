import numpy as np
import pandas as pd

class FairnessMetrics:
    """
    Implementation of the Integrated Multilingual Fairness Framework metrics.
    """

    def __init__(self, dataframe): # اصلاح از init__ به __init__
        self.df = dataframe

    def calculate_fqi(self, model_name=None, prompt_condition=None):
        filtered_df = self.df
        if model_name:
            filtered_df = filtered_df[filtered_df['Model'] == model_name]
        if prompt_condition:
            filtered_df = filtered_df[filtered_df['Prompt'] == prompt_condition]
        
        # استفاده از mean استاندارد
        return round(filtered_df['Overall_Score'].mean(), 3)

    def calculate_mfi(self, model_name=None, prompt_condition=None):
        filtered_df = self.df
        if model_name:
            filtered_df = filtered_df[filtered_df['Model'] == model_name]
        if prompt_condition:
            filtered_df = filtered_df[filtered_df['Prompt'] == prompt_condition]

        # گروه‌بندی بر اساس زبان مادری
        l1_means = filtered_df.groupby('L1_Background')['Overall_Score'].mean()
        global_mean = l1_means.mean()
        std_dev_l1 = l1_means.std()

        if global_mean == 0 or pd.isna(std_dev_l1):
            return 0

        # MFI Calculation
        mfi_score = 1 - (std_dev_l1 / global_mean)
        return round(float(mfi_score), 3)

    def get_l1_breakdown(self, model_name=None):
        filtered_df = self.df
        if model_name:
            filtered_df = filtered_df[filtered_df['Model'] == model_name]
        return filtered_df.groupby('L1_Background')['Overall_Score'].mean().to_dict()
