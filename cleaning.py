import pandas as pd

def clean_data():
    df = pd.read_csv("diabetes_prediction_dataset.csv")

    df = df.drop_duplicates()

    df.to_csv("cleaned_diabetes_dataset.csv", index=False)

    return df