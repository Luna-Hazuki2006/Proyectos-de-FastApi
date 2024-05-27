from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post('/archivos')
async def crear_archivo(file : Annotated[bytes, File()]): 
    return {"tamaño_archivo": len(file)}

@app.post('/Subir_archivo')
async def subir_archivo(file : UploadFile): 
    return {'nombre_archivo': file.filename}