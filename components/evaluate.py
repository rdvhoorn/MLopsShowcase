import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow

# Load the test dataset
test_data = pd.read_csv('data/test.csv')
X_test = test_data.drop('target', axis=1)
Y_test = test_data['target']

# Load the trained model
model = joblib.load('models/best_model.pkl')

# Predict on the test set
predictions = model.predict(X_test)

# Compute evaluation metrics
accuracy = accuracy_score(Y_test, predictions)
precision = precision_score(Y_test, predictions, average='weighted')
recall = recall_score(Y_test, predictions, average='weighted')
f1 = f1_score(Y_test, predictions, average='weighted')

# Print the results
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Log the evaluation metrics to MLflow
mlflow.log_metric('accuracy', accuracy)
mlflow.log_metric('precision', precision)
mlflow.log_metric('recall', recall)
mlflow.log_metric('f1_score', f1) 