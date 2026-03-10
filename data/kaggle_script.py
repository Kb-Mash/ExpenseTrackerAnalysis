import kagglehub

# Download latest version
path = kagglehub.dataset_download("abutalhadmaniyar/bank-statements-dataset")

print("Path to dataset files:", path)