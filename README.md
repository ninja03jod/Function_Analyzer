# Function Analyzer API

## Overview
This API analyzes Python and JavaScript functions using the Llama3 model.

## Project Structure
- `app/main.py`: Main FastAPI application
- `Dockerfile`: Dockerfile for building the Docker image
- `requirements.txt`: Python dependencies

### 1. Clone the Repository
```bash
git clone https://github.com/ninja03jod/Function_Analyzer
cd Function_Analyzer
```

### 2. Build the Docker Image
```bash
docker build -t function_analyzer .
```

### 3. Run the Docker Container
```bash
docker run -d -p 8000:8000 function_analyzer
```

### 4. Access the FastAPI Application

`API Documentation:` API documentation is accessible via Swagger UI at
`/docs` endpoint. You can view it at `http://localhost:8000/docs` when
running the application.

### 5. Pulling a Pre-built Docker Image
```bash
docker pull 840804/function_analyzer
```
```bash
docker run -d -p 8000:8000 840804/function_analyzer
```

### Contact
For questions or issues, please contact `saadbagwan447@gmail.com`

### Explanation:
- **Clone the Repository**: Instructions to get the code from your version control system.
- **Build the Docker Image**: How to build the Docker image from the `Dockerfile`.
- **Run the Docker Container**: Instructions to start the container and map the ports.
- **Pulling a Pre-built Docker Image**: How to pull and run an existing Docker image if it's hosted on Docker Hub.
- **API Endpoints**: Example endpoints for interacting with the FastAPI application.
