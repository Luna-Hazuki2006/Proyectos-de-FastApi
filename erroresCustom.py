from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

class CustomException(Exception): 
    def __init__(self, name: str):
        self.name = name 

app = FastAPI()

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc : CustomException): 
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT, 
        content= {'message': f"I'm a teapot! I can not make this coffe: {exc.name}"}
    )

@app.get('/exception/{name}')
async def custom_exception(name : str): 
    if name == "pedro": raise CustomException(name="No puedo hacer café :(")
    return {'name': name}