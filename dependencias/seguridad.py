from typing import Annotated, Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oath_sistema = OAuth2PasswordBearer(tokenUrl='token')

@app.get('/items')
async def leer_items(token: Annotated[str, Depends(oath_sistema)]): 
    return {'token': token}

usuarios_falsos_bd = {
    'Ana': {
        'usuario' : 'Ana', 
        'correo' : 'anapaulamendozadiaz2006@gmail.com', 
        'nombre_completo' : 'Ana Paula Mendoza Díaz', 
        'desabilitado' : True
    }, 
    'Luna': {
        'usuario' : 'Luna', 
        'correo' : 'lunahazuki2006@outlook.com', 
        'nombre_completo' : 'Luna Hazuki', 
        'desabilitado' : True
    }
}

class Usuario(BaseModel): 
    usuario : str
    correo : Union[str, None] = None
    nombre_completo : Union[str, None] = None
    desabilitado : Union[bool, None] = None

class UsuarioBD(Usuario): 
    contraseña_encriptada : str

def obtener_usuario(bd, usuario : str): 
    if usuario in bd: 
        usuario_dic = bd[usuario]
        return UsuarioBD(**usuario_dic)

def token_falso_decodificar(token): 
    return Usuario(
        usuario=token + 'codigofalso', 
        correo='anapaulamendozadiaz2006@gmail.com', 
        nombre_completo='Ana Paula Mendoza Díaz'
    )

def encriptado_token_falso(contraseña : str): 
    return 'falsoencriptado' + contraseña

async def obtner_usuario_actual(token : Annotated[str, Depends(oath_sistema)]): 
    usuario = token_falso_decodificar(token)
    return usuario

@app.get('/usuario/yo')
async def leer_usuario_yo(usuario_actual: Annotated[Usuario, Depends(obtner_usuario_actual)]): 
    return usuario_actual 

@app.post('/token')
async def iniciar(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]): 
    usuario_dic = usuarios_falsos_bd.get(form_data.username)
    if not usuario_dic: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Usuario o contraseña incorrecta'
        )
    usuario = UsuarioBD(**usuario_dic)
    contraseña_encriptada = encriptado_token_falso(form_data.password)
    if not contraseña_encriptada == usuario.contraseña_encriptada: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Usuario o contraseña incorrecta'
        )
    return {'token_acceso': usuario.usuario, 'tipo_token': 'bearer'}