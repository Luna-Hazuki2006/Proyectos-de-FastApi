from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = {'foo': 'El panda foo'}

@app.get('/items/{id}')
async def listar(id : str): 
    if id not in items: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El item no esta en la lista")
    return {"item": items[id]}