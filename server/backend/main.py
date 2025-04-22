from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger(__name__)

# Load configuration from environment variables
MODEL_PATH = os.getenv('MODEL_PATH', 'models/best_model.pkl')
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', '8000'))

# Load the trained model
try:
    model = joblib.load(MODEL_PATH)
    logger.info(f"Successfully loaded model from {MODEL_PATH}")
except Exception as e:
    logger.error(f"Failed to load model from {MODEL_PATH}: {str(e)}")
    raise

# Define the FastAPI app
app = FastAPI(
    title="Iris Classification API",
    description="API for classifying iris flowers",
    version="1.0.0"
)

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
    try:
        # Convert input to numpy array
        X = np.array([[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width] for item in input_data.data])
        
        # Make predictions
        predictions = model.predict(X)

        # Map predictions to target names
        target_names = ['setosa', 'versicolor', 'virginica']
        predicted_names = [target_names[pred] for pred in predictions]

        logger.info(f"Successfully made predictions for {len(predictions)} samples")
        return {"predictions": predicted_names}
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting server on {HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)