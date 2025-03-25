import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib
import os
import mlflow.sklearn

# Enable autologging
mlflow.sklearn.autolog()

# Start an MLflow run
# with mlflow.start_run():
    # Load training data
train_df = pd.read_csv('data/train.csv')
X_train = train_df.drop('target', axis=1)
y_train = train_df['target']

# Define models and parameters
models = {
    'RandomForest': RandomForestClassifier(),
    'SVC': SVC()
}

params = {
    'RandomForest': {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 10, 20]
    },
    'SVC': {
        'C': [0.1, 1, 10],
        'kernel': ['linear', 'rbf']
    }
}

# Train models and tune hyperparameters
best_model = None
best_score = 0

for model_name, model in models.items():
    # Start an MLflow run for each model
    with mlflow.start_run(run_name=model_name):
        clf = GridSearchCV(model, params[model_name], cv=5, scoring='accuracy')
        clf.fit(X_train, y_train)
        
        if clf.best_score_ > best_score:
            best_score = clf.best_score_
            best_model = clf.best_estimator_

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Save the best model
joblib.dump(best_model, 'models/best_model.pkl')

print(f"Best model: {best_model}")
print(f"Best score: {best_score}") 