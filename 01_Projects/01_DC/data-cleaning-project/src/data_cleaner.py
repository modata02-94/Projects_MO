import pandas as pd


class DataCleaner:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self, filepath):
        try:
            df = pd.read_csv(filepath)
            return df
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            raise

    def clean_data(self, filepath):
        # Drop null values
        df = df.dropna(axis=1)
        # Remove duplicates
        df = df.drop_duplicates()
        # Handle outliers
        for col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

        # Data type corrections
        # xxx
        
    def save_data(self, df, filepath):
        df.to_csv(filepath)