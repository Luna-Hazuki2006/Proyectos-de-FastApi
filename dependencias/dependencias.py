from typing import Annotated
from fastapi import Depends, FastAPI, Header, HTTPException, status

app = FastAPI()

cositas = [{"item_name": "One"}, {"item_name": "Two"}, {"item_name": "Three"}]

class ParametrosQueryComunes: 
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get('/items')
async def leer_items(comunes: Annotated[ParametrosQueryComunes, Depends(ParametrosQueryComunes)]): 
    respuesta = {}
    if comunes.q: 
        respuesta.update({"q": comunes.q})
    datos = cositas[comunes.skip: comunes.skip + comunes.limit]
    respuesta.update({'items': datos})
    return respuesta

def ultimo_usuario(apellido: Annotated[str, Header()]): 
    return apellido

class Usuario: 
    def __init__(
            self, 
            nombre: str, 
            apellido: Annotated[str, Depends(ultimo_usuario)]
    ) -> None:
        self.nombre = nombre
        self.apellido = apellido

    @property
    def nombre_completo(self) -> str: 
        return f'{self.nombre} {self.apellido}'
    
@app.post('/holis')
def hola(usuario: Annotated[Usuario, Depends(Usuario)]): 
    return f'Holis {usuario.nombre_completo}'

@app.post('/chao')
def chao(apellido: str = Depends(ultimo_usuario)): 
    return f'Chau {apellido}'

async def verificar_token(x_token: Annotated[str, Header()]): 
    if x_token != 'mi secreto mas íntimo': 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El token del header es inválido"
        )
    
async def verificar_llave(x_llave: Annotated[str, Header()]): 
    if x_llave != 'mi secreto mas íntimo': 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='La llave del header es inválida'
        )
    
@app.get('/cositas', dependencies=[Depends(verificar_token), Depends(verificar_llave)])
async def leer_cositas(): 
    return [{'hola': 'mundo', 'Emma': 'Elios'}]