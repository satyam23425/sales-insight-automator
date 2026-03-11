# Sales Insight Automator

Python based automation system that analyzes sales data and generates insights.

## Features

- Sales data analysis
- REST API using FastAPI
- Docker containerization
- CI/CD using GitHub Actions
- Simple frontend dashboard

## Run Locally

pip install -r requirements.txt

uvicorn app.main:app --reload

## Docker

docker build -t sales-automator .

docker run -p 8000:8000 sales-automator