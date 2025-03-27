import streamlit as st
import pandas as pd
import requests
import json

# Section 1: Title + brief description
st.title('Iris Prediction App')
st.write('This app predicts the class of an Iris flower based on its features.')

# Section 2: Model metrics
st.header('Model Metrics')
with open('frontend/metrics.json', 'r') as f:
    metrics = json.load(f)

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

    # Call the FastAPI backend
    response = requests.post('http://localhost:8000/predict', json=input_data)
    prediction = response.json()['predictions'][0]

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