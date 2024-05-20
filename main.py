from fastapi import FastAPI

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
async def read_items(skip: int = 3, limit: int = 10): 
    return [{skip: skip + limit}]

@app.get('/greet/{nombre}')
def greet(nombre : str) -> str:
    return f'hola {nombre}'

