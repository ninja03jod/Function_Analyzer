# Function Analyzer API

## Overview
This API analyzes Python and JavaScript functions using the Llama3 model.

## Project Structure
- `app/main.py`: Main FastAPI application
- `app/api.py`: API route definitions
- `app/model.py`: LLM model integration
- `app/utils.py`: Utility functions
- `app/test_cases.py`: Test cases for the API
- `Dockerfile`: Dockerfile for building the Docker image
- `requirements.txt`: Python dependencies

## How to Run
1. Build the Docker image:
   ```sh
   docker build -t function-analyzer .
