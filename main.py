from fastapi import FastAPI, Path, status, Request, Form
from validaciones import Item
from typing import Annotated, Any
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

lista = [{'item_nombre': 'Uno'}, {'item_nombre': 'Dos'}, {'item_nombre': 'Tres'}]

@app.get('/')
def home(): 
    return {'mensaje': 'Hola mundo'}

@app.get('/itemsInt/{id}', response_class=HTMLResponse)
async def read_item(request : Request, id : str): 
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get('/form')
def get_form(request : Request): 
    result = "Ingrese un número"
    return templates.TemplateResponse(
        name="formitem.html", context={'request': request, 'result': result}
    )

@app.post('/form')
def post_form(request : Request, numero : int = Form(...)): 
    result = numero
    return templates.TemplateResponse(
        name="formitem.html", context={'request': request, 'result': result}
    )

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

