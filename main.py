from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from transformers import pipeline

app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head><title>Sentiment App</title></head>
        <body>
            <h1>Test sentiment</h1>
            <form method="post" action="/predict">
                <input name="text" type="text" size="60">
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.post("/predict")
async def predict(text: str = Form(...)):
    result = classifier(text)
    return {"prediction": result}
