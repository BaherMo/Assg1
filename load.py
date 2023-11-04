# load.py

import pandas as pd
import sys

def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully:")
        print(data.head())  # Display the first few rows of the dataset
    except Exception as e:
        print("Error loading the dataset:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the file path as an argument.")
    else:
        file_path = sys.argv[1]
        load_dataset(file_path)
