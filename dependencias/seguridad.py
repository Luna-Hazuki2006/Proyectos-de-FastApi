from typing import Annotated, Union
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oath_sistema = OAuth2PasswordBearer(tokenUrl='token')

@app.get('/items')
async def leer_items(token: Annotated[str, Depends(oath_sistema)]): 
    return {'token': token}

class Usuario(BaseModel): 
    usuario : str
    correo : Union[str, None] = None
    nombre_completo : Union[str, None] = None
    desabilitado : Union[bool, None] = None

def token_falso_decodificar(token): 
    return Usuario(
        usuario=token + 'codigofalso', 
        correo='anapaulamendozadiaz2006@gmail.com', 
        nombre_completo='Ana Paula Mendoza Díaz'
    )

async def obtner_usuario_actual(token : Annotated[str, Depends(oath_sistema)]): 
    usuario = token_falso_decodificar(token)
    return usuario

@app.get('/usuario/yo')
async def leer_usuario_yo(usuario_actual: Annotated[Usuario, Depends(obtner_usuario_actual)]): 
    return usuario_actual