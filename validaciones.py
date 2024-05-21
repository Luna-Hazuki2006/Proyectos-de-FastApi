from pydantic import BaseModel, ValidationError, field_validator, Field
from typing import Optional

class Usuario(BaseModel): 
    usuario : str
    contraseña : str = Field(min_length=4)
    correo : str
    edad : Optional[int] = None

    @field_validator('usuario')
    def tamaño(cls, usuario): 
        if len(usuario) < 4: raise ValueError('La longitud mínima es de 4 caracteres')
        elif len(usuario) > 20: raise ValueError('La longitud máxima es de 20 caracteres')
        return usuario
    
class Item(BaseModel): 
    nombre: str
    descripcion: str | None = None
    precio: float
    impuesto: float | None = None


user = Usuario(usuario='LunaHazuki', contraseña='1234', correo='lunahazuki2006@outlook.com', edad=13)
user2 = Usuario(usuario='LunaHazuki', contraseña='1234', correo='lunahazuki2006@outlook.com')

print(f'usuario {user}')
print(f'usuario {user2}')

try: 
    user3 = Usuario(usuario='LunaHazuki', contraseña='1234')
    print(f'usuario {user3}')
except ValidationError as e: 
    print(e.json())

try: 
    user3 = Usuario(usuario='LunaHazukidjfaoisdejfwqeijtfqpiwjefiterjtgijrew0gitwjer0g9tiwejr09tgwj', contraseña='1234', correo='lunahazuki2006@outlook.com')
    print(f'usuario {user3}')
except ValidationError as e: 
    print(e.json())

try: 
    user3 = Usuario(usuario='LunaHazuki', contraseña='134', correo='lunahazuki2006@outlook.com')
    print(f'usuario {user3}')
except ValidationError as e: 
    print(e.json())