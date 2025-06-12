FROM python:3.10-slim

RUN pip install fastapi uvicorn transformers torch

COPY . /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
