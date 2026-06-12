import pandas as pd


def load_retail_data(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)


def profile_data(df: pd.DataFrame) -> None:
    print("\nDataset Shape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isna().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nNumeric Summary:")
    print(df.describe())

    print("\nCountry Count:")
    print(df["Country"].value_counts().head(10))


if __name__ == "__main__":
    file_path = "data/sample/online_retail.xlsx"
    df = load_retail_data(file_path)
    profile_data(df)