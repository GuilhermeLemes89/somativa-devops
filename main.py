from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/apresentacao")
async def apresentar():
    return {"Atividade Somativa - DEVOPS"}

@app.get("/aleatorio")
async def numeroaleatorio():
    return {"num_altr": random.randint(0, 1000)}

@app.get("/site", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>PUC-PR</title>
        </head>
        <body>
            <h1>Disciplina: DEVOPS</h1>
            <p>Pequeno site para teste.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


