# -----------------------------
# Codespaces + uv + KaggleHub script
# -----------------------------

import os
import sys
import subprocess

# 1️⃣ Install kagglehub inside uv if not installed
try:
    import kagglehub
    import pandas as pd
except ImportError:
    print("Installing kagglehub and dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "kagglehub[pandas-datasets]"])
    import kagglehub
    import pandas as pd

# 2️⃣ Check for Kaggle API environment variables
username = os.getenv("KAGGLE_USERNAME")
key = os.getenv("KAGGLE_KEY")

if not (username and key):
    raise ValueError(
        "Kaggle API credentials not found! "
        "Set KAGGLE_USERNAME and KAGGLE_KEY in Codespaces environment variables."
    )

# 3️⃣ Dataset slug
dataset_slug = "abutalhadmaniyar/bank-statements-dataset"

# 4️⃣ Download the dataset
print(f"Downloading dataset: {dataset_slug} ...")
dataset_path = kagglehub.dataset_download(dataset_slug)
print("Dataset downloaded to:", dataset_path)

# 5️⃣ List files and pick the first CSV
files = [f for f in os.listdir(dataset_path) if f.endswith(".csv")]
if not files:
    raise ValueError("No CSV file found in the dataset!")
csv_file = os.path.join(dataset_path, files[0])
print("Using CSV file:", csv_file)

# 6️⃣ Load CSV into Pandas
df = pd.read_csv(csv_file)
print("First 5 records:")
print(df.head())