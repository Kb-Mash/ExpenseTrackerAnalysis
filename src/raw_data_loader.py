import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_raw_data():
    return pd.read_csv(DATA_DIR / "personal_expense_dataset.csv")