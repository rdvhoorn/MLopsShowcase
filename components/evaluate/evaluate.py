import argparse
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json
import os

def evaluate_model(model_path: str, test_data_path: str, metrics_path: str) -> str:
    """Evaluate the model and return the path to the metrics file."""
    # Load the model and test data
    model = joblib.load(model_path)
    test_df = pd.read_csv(test_data_path)
    
    X_test = test_df.drop('target', axis=1)
    y_test = test_df['target']
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, average='weighted'),
        'Recall': recall_score(y_test, y_pred, average='weighted'),
        'F1 Score': f1_score(y_test, y_pred, average='weighted')
    }
    
    # Save metrics to JSON
    os.makedirs(os.path.dirname(metrics_path), exist_ok=True)
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    
    return metrics_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--test_data_path", type=str, required=True)
    parser.add_argument("--metrics_path", type=str, required=True)
    args = parser.parse_args()

    evaluate_model(args.model_path, args.test_data_path, args.metrics_path) 
