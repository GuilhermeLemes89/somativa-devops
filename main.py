from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Lá vem o Chaves"}

@app.get("/apresentacao")
async def apresentar():
    return {"Atividade Somativa 2 - DEVOPS"}

@app.get("/aleatorio")
async def numeroaleatorio():
    return {"num_altr": random.randint(0, 5000)}



