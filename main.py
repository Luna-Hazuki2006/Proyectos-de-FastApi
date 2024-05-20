from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home(): 
    return {'mensaje': 'Hola mundo'}

@app.get('/items/{item_id}')
async def read_item(item_id : int): 
    return {'item_id': item_id}

print('hola')