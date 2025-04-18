import argparse
import pandas as pd
from sklearn.datasets import load_iris
import os

from sklearn.model_selection import train_test_split

def download_data(train_data_path: str, test_data_path: str):
    """Download the Iris dataset and save it as a CSV file."""
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Convert to DataFrame
    train_df = pd.DataFrame(X_train, columns=iris.feature_names)
    train_df['target'] = y_train
    test_df = pd.DataFrame(X_test, columns=iris.feature_names)
    test_df['target'] = y_test

    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    # Save to CSV
    train_df.to_csv(train_data_path, index=False)
    test_df.to_csv(test_data_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_data_path", type=str, required=True)
    parser.add_argument("--test_data_path", type=str, required=True)
    args = parser.parse_args()

    download_data(args.train_data_path, args.test_data_path)