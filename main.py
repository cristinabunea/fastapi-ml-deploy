from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.post("/predict")
async def predict(request: Request):
    body = await request.json()
    text = body.get("text", "")
    result = classifier(text)
    return {"prediction": result}
