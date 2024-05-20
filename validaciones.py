from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel): 
    usuario : str
    contraseña : str
    correo : str
    edad : Optional[int] = None


user = Usuario(usuario='LunaHazuki', contraseña='1234', correo='lunahazuki2006@outlook.com', edad=13)