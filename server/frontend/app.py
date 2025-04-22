import streamlit as st
import pandas as pd
import requests
import json
import os
import logging

# Configure logging
logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger(__name__)

# Load configuration from environment variables
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:9000')
METRICS_PATH = os.getenv('METRICS_PATH', 'metrics.json')

# Section 1: Title + brief description
st.title('Super cool Prediction App')
st.write('This app predicts the class of an Iris flower based on its features.')

# Section 2: Model metrics
st.header('Model Metrics')
try:
    with open(METRICS_PATH, 'r') as f:
        metrics = json.load(f)
    logger.info(f"Successfully loaded metrics from {METRICS_PATH}")
except Exception as e:
    logger.error(f"Failed to load metrics from {METRICS_PATH}: {str(e)}")
    st.error("Failed to load model metrics. Please check the configuration.")
    metrics = {}

# Create a 2x2 grid for metrics
col1, col2 = st.columns(2)

# Display metrics in the grid
for i, (metric_name, value) in enumerate(metrics.items()):
    if i < 2:
        with col1:
            st.metric(metric_name, f"{value:.2f}")
    else:
        with col2:
            st.metric(metric_name, f"{value:.2f}")

# Section 3: Input form with 4 sliders
st.header('Input Features')

# Create a 2x2 grid for sliders
col1, col2 = st.columns(2)

# Display sliders in the grid
with col1:
    sepal_length = st.slider('Sepal Length', min_value=0.0, max_value=10.0, value=5.0)
    sepal_width = st.slider('Sepal Width', min_value=0.0, max_value=10.0, value=3.0)

with col2:
    petal_length = st.slider('Petal Length', min_value=0.0, max_value=10.0, value=4.0)
    petal_width = st.slider('Petal Width', min_value=0.0, max_value=10.0, value=1.5)

# Section 4: Button to send prediction req
if st.button('🔍 Predict', use_container_width=True):
    # Prepare input data
    input_data = {
        "data": [
            {
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width
            }
        ]
    }

    try:
        # Call the FastAPI backend
        logger.info(f"Making prediction request to {BACKEND_URL}/predict")
        response = requests.post(f'{BACKEND_URL}/predict', json=input_data)
        response.raise_for_status()
        prediction = response.json()['predictions'][0]
        logger.info(f"Received prediction: {prediction}")

        # Section 5: Display predicted class
        st.markdown("---")  # Add a separator line
        st.markdown("### 🌸 Prediction Result")
        
        # Create a container for the prediction
        pred_container = st.container()
        with pred_container:
            # Add a colored background based on the prediction
            color = {
                'setosa': '#FFB6C1',      # Light pink
                'versicolor': '#98FB98',  # Light green
                'virginica': '#87CEEB'    # Light blue
            }.get(prediction, '#FFFFFF')
            
            st.markdown(f"""
                <div style='background-color: {color}; padding: 20px; border-radius: 10px; text-align: center;'>
                    <h2 style='color: #2c3e50; margin: 0;'>{prediction.capitalize()}</h2>
                </div>
            """, unsafe_allow_html=True)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making prediction request: {str(e)}")
        st.error("Failed to get prediction from the backend. Please try again later.")
    except Exception as e:
        logger.error(f"Unexpected error during prediction: {str(e)}")
        st.error("An unexpected error occurred. Please try again later.") 