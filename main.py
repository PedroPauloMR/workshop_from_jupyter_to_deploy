from fastapi import FastAPI
from typing import List, Dict


app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id":1,
        "nome":"Smartphone",
        "descricao":"Um telefone que é inteligente",
        "preco":1500.00,
    },
    {
        "id":2,
        "nome":"Notebook",
        "descricao":"Um computador que é móvel",
        "preco":3500.00,
    },
    {
        "id":3,
        "nome":"Tablet",
        "descricao":"Um computador que é móvel",
        "preco":2500.00,
    },
]


@app.get("/")
def ola_mundo():
    return {'Olá':'Mundo'}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{id}")
def buscar_produto(id: int):
    for produto in produtos:
        if produto['id'] == id:
            return produto
    return {'Status': 404, 'Mensagem': "Produto não encontrado"}