from fastapi import FastAPI
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



