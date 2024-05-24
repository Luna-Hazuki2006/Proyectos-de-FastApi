from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

@app.post('/login')
async def login(usuario: Annotated[str, Form()], clave: Annotated[str, Form()]): 
    return {"usuario": usuario, 'clave': clave}