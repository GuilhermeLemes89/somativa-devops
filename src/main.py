from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI()

class Colaborador(BaseModel):
    name: str
    setor: str
    ativo: bool


@app.get("/")
async def root():
    return {"message": "Lá vem o Chaves"}

@app.get("/apresentacao")
async def apresentar():
    return {"Atividade Somativa 2 - DEVOPS"}

@app.get("/aleatorio")
async def numeroaleatorio():
    return {"num_altr": random.randint(0, 5000)}

@app.post("/colaboradores/cadastro")
async def create_colaborador(colaborador: Colaborador):
    return colaborador

@app.put("/colaboradores/update/{id_colaborador}")
async def update_colaborador(id_colaborador: int):
    return id_colaborador > 0

@app.delete("/colaboradores/delete/{id_colaborador}")
async def delete_colaborador(id_colaborador: int):
    return id_colaborador > 0

