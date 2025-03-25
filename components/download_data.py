import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import os

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split into train/test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert to DataFrame
train_df = pd.DataFrame(X_train, columns=iris.feature_names)
train_df['target'] = y_train

test_df = pd.DataFrame(X_test, columns=iris.feature_names)
test_df['target'] = y_test

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save to CSV
train_df.to_csv('data/train.csv', index=False)
test_df.to_csv('data/test.csv', index=False) 
