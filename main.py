from fastapi import FastAPI, Path, status
from validaciones import Item
from typing import Annotated, Any

app = FastAPI()

lista = [{'item_nombre': 'Uno'}, {'item_nombre': 'Dos'}, {'item_nombre': 'Tres'}]

@app.get('/')
def home(): 
    return {'mensaje': 'Hola mundo'}

@app.get('/itemsInt/{item_id}')
async def read_item(item_id : int): 
    return {'item_id': item_id}

@app.get('/items/{item_id}')
async def read_item(item_id): 
    return {'item_id': item_id}

@app.get('/items/')
async def read_items() -> Any: 
    return [
        Item(nombre="granito", precio=4.5), 
        Item(nombre="Obsidiana", precio=10)
    ]

@app.post('/items/', status_code=status.HTTP_201_CREATED)
async def create_item(item : Item): 
    return item

@app.put('/items/{item_id}')
async def update_item(
    item_id : Annotated[int, Path(title="ID del item", ge=0, le=1000)], 
    q : str | None = None, 
    item : Item | None  = None
):
    resultados = {"item_id": item_id}
    if q: resultados.update({"q": q})
    if item: resultados.update({"item": item})
    return resultados



@app.get('/greet/{nombre}')
def greet(nombre : str) -> str:
    return f'hola {nombre}'

