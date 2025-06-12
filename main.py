from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from transformers import pipeline
import uvicorn

app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head><title>Sentiment Tester</title></head>
        <body>
            <h2>Enter text to analyze:</h2>
            <form action="/predict" method="post">
                <input name="text" type="text" size="60"/>
                <input type="submit"/>
            </form>
        </body>
    </html>
    """

@app.post("/predict")
async def predict(text: str = Form(...)):
    result = classifier(text)
    return {"prediction": result}
