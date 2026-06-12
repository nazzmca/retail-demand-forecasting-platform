import pandas as pd


def load_retail_data(file_path: str) -> pd.DataFrame:
    """Load retail sales data from a CSV file."""
    return pd.read_csv(file_path)


if __name__ == "__main__":
    print("Retail data ingestion module ready.")