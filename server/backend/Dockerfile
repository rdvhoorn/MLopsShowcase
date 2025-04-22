# Use Python 3.9 slim image as base
FROM robinvhoorn/mlops-showcase-base:latest

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install fastapi uvicorn scikit-learn pydantic

# Copy the rest of the application
COPY . .

# Set default environment variables
ENV MODEL_PATH=/app/models/best_model.pkl
ENV HOST=0.0.0.0
ENV PORT=8000
ENV LOG_LEVEL=INFO

# Expose the port the app runs on
EXPOSE 9000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"] 