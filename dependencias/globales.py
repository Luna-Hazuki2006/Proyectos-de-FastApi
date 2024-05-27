from typing_extensions import Annotated
from fastapi import Depends, FastAPI, Header, HTTPException, status

cositas = [{"item_name": "One"}, {"item_name": "Two"}, {"item_name": "Three"}]

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

app = FastAPI(dependencies=[Depends(verificar_token), Depends(verificar_llave)])
    
@app.get('/cositas')
async def leer_cositas(): 
    return [{'hola': 'mundo', 'Emma': 'Elios'}]

@app.get('/usuarios')
async def usuarios(): 
    return [{'Emma': 'Elios', 'Elios': 'Emma'}]