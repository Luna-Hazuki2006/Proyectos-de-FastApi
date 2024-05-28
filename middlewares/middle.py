import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware('http')
async def añadir_proceso_tiempo_header(request : Request, call_next): 
    inicio_tiempo = time.time()
    response = await call_next(request)
    tiempo_proceso = time.time() - inicio_tiempo
    response.headers['X-Process-Time'] = str(tiempo_proceso)
    return response