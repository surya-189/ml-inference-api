# ML Inference API

A lightweight machine-learning inference service built with Python, FastAPI and scikit-learn.

This project demonstrates how a trained machine-learning model can be integrated into a REST-based inference service, including input validation, health checks, automated testing, containerisation and continuous integration.

## Architecture

Client  
↓  
**FastAPI REST API**  
↓  
**Input Validation**  
↓  
**Persisted Machine-Learning Model**  
↓  
**Prediction + Confidence**

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

**Endpoint**

`GET /health`

**Example response**

```json
{
  "status": "healthy"
}
```

### Prediction

**Endpoint**

`POST /predict`

**Request**

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

**Example response**

```json
{
  "prediction": 0,
  "confidence": 0.9847
}
```

## Running Locally

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train_model.py
```

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

### 5. Open the API documentation

Open:

`http://127.0.0.1:8000/docs`

FastAPI provides interactive Swagger documentation for testing the API endpoints.

## Testing

Run the automated tests:

```bash
pytest
```

The tests cover:

- Health endpoint
- Successful model inference
- Invalid input validation

## Docker

### Build the container

```bash
docker build -t ml-inference-api .
```

### Run the container

```bash
docker run --rm -p 8000:8000 ml-inference-api
```

### Open the API documentation

Open:

`http://localhost:8000/docs`

## Continuous Integration

GitHub Actions automatically performs the following steps:

1. Checks out the source code
2. Sets up Python 3.12
3. Installs project dependencies
4. Runs the automated test suite
5. Builds the Docker image

This provides a basic CI validation pipeline for the inference service.

## Production Considerations

For a production ML inference platform, this service could be extended with:

- Model registry and version management
- Model version tracking
- Authentication and authorisation
- Structured application logging
- Metrics and observability
- Model performance monitoring
- Data and model drift detection
- Container image security scanning
- Automated deployment
- Horizontal scaling
- Secure secret management
- Model rollback and controlled releases

These are identified as potential production enhancements and are not claimed as implemented features of this demonstration project.

## Project Scope

This is a deliberately small demonstration project designed to demonstrate the engineering pattern of integrating a machine-learning model into an inference service.

The project demonstrates:

- Machine-learning model training
- Model persistence
- REST API-based inference
- Input validation
- Prediction confidence
- Automated testing
- Docker containerisation
- Continuous integration

The Iris dataset and model are used to demonstrate the engineering pattern rather than represent a production mission workload.

## Repository Structure

```text
ml-inference-api/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_api.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── model.joblib
├── pytest.ini
├── requirements.txt
├── train_model.py
└── README.md
```

## Summary

This project demonstrates an end-to-end machine-learning inference pattern using Python, FastAPI and scikit-learn.

The trained model is exposed through a REST API, validated through automated tests, packaged as a Docker container and validated through GitHub Actions CI.