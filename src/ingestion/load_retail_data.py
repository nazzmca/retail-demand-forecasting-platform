import pandas as pd


def load_retail_data(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)


if __name__ == "__main__":
    file_path = "data/sample/online_retail.xlsx"

    df = load_retail_data(file_path)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())