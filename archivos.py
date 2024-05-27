from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post('/archivos')
async def crear_archivo(files : Annotated[list[bytes], File()]): 
    return {"tamaño_archivo": [len(file) for file in files]}

@app.post('/Subir_archivo')
async def subir_archivo(files : list[UploadFile]): 
    return {'nombre_archivo': [file.filename for file in files]}