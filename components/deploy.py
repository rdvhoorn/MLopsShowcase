from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load('models/best_model.pkl')

# Define the FastAPI app
app = FastAPI()

# Define the input data model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisInputList(BaseModel):
    data: list[IrisInput]

# Define the /predict endpoint
@app.post("/predict")
async def predict(input_data: IrisInputList):
    # Convert input to numpy array
    X = np.array([[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width] for item in input_data.data])
    
    # Make predictions
    predictions = model.predict(X)

    # Map predictions to target names
    target_names = ['setosa', 'versicolor', 'virginica']
    predicted_names = [target_names[pred] for pred in predictions]

    # Return the predicted names
    return {"predictions": predicted_names} 