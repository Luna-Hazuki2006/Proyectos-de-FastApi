from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status

app = FastAPI()

data = {
    'plumbus': {'descripcion': 'Un fresco nuevo plumbus', 'dueño': 'Morty'}, 
    'pistola-portal': {'descripcion': 'Pistola que crea portales', 'dueño': 'Rick'}
}

class DueñoError(Exception): 
    pass

def buscar_usuario(): 
    try: 
        yield 'Rick'
    except DueñoError as e: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'Error de dueño: {e}'
        )
    
@app.get('/cositas/{id}')
def buscar_cosa(id: str, usuario: Annotated[str, Depends(buscar_usuario)]): 
    if id not in data: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='La cosa no fue encontrada'
        )
    cosa = data[id]
    if cosa['dueño'] != usuario: 
        raise DueñoError(usuario)
    return cosa