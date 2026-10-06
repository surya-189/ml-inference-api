# ML Inference API

A lightweight machine-learning inference service built with Python, FastAPI and scikit-learn.

This project demonstrates how a trained machine-learning model can be integrated into a REST-based inference service, including input validation, health monitoring, automated testing, containerisation and continuous integration.

## Architecture

Client
  |
  | POST /predict
  v
FastAPI REST API
  |
  | Validate Input
  v
Persisted ML Model
  |
  v
Prediction + Confidence

## Technology Stack

- Python 3.12
- FastAPI
- Pydantic
- scikit-learn
- joblib
- pytest
- Docker
- GitHub Actions

## Machine Learning Model

The project uses the Iris dataset and a Logistic Regression classification model.

The training pipeline applies feature standardisation before classification.

The trained model is persisted as `model.joblib` and loaded by the FastAPI inference service when the application starts.

## API

### Health Check

GET /health

Example response:

{
  "status": "healthy"
}

### Prediction

POST /predict

Request:

{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Example response:

{
  "prediction": 0,
  "confidence": 0.9847
}

## Running Locally

Create a virtual environment:

    python -m venv .venv

Activate the environment and install dependencies:

    pip install -r requirements.txt

Train the model:

    python train_model.py

Start the API:

    uvicorn app.main:app --reload

Open the interactive API documentation:

    http://127.0.0.1:8000/docs

## Testing

Run the automated tests:

    pytest

The tests cover:

- Health endpoint
- Successful model inference
- Invalid input validation

## Docker

Build the container:

    docker build -t ml-inference-api .

Run the container:

    docker run --rm -p 8000:8000 ml-inference-api

Open the API documentation:

    http://localhost:8000/docs

## Continuous Integration

GitHub Actions automatically:

1. Checks out the source code
2. Sets up Python
3. Installs dependencies
4. Runs automated tests
5. Builds the Docker image

## Production Considerations

For a production ML inference platform, the service could be extended with:

- Model registry and version management
- Authentication and authorisation
- Structured logging
- Metrics and observability
- Model performance monitoring
- Data and model drift detection
- Container image security scanning
- Automated deployment
- Horizontal scaling
- Secure secret management
- Model rollback and controlled releases

## Project Scope

This is a deliberately small demonstration project designed to demonstrate ML model integration and inference engineering.

The Iris dataset and model are used to demonstrate the engineering pattern rather than represent a production mission workload.