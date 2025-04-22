# Use Python 3.9 slim image as base
FROM robinvhoorn/mlops-showcase-base:latest

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install streamlit pandas requests

# Copy the application files
COPY . .

# Set default environment variables
ENV BACKEND_URL=http://backend:9000
ENV METRICS_PATH=metrics.json
ENV LOG_LEVEL=INFO
ENV STREAMLIT_SERVER_PORT=80
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Expose the port the app runs on
EXPOSE 80

# Command to run the application using shell form to allow env var substitution
CMD streamlit run app.py --server.port=${STREAMLIT_SERVER_PORT} --server.address=${STREAMLIT_SERVER_ADDRESS} 