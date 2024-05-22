from pydantic import BaseModel, ValidationError, field_validator, Field
from typing import Optional
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

class Usuario(BaseModel): 
    usuario : str
    contraseña : str = Field(min_length=4)
    correo : str
    edad : int

    @field_validator('usuario')
    def nombre(cls, usuario): 
        if len(usuario) <= 0: raise ValueError('El nombre de usario no puede estar vacío')
        return usuario
    @field_validator('edad')
    def vejez(cls, edad): 
        if edad < 18: raise ValueError('La no puede ser menor a 18')
        return edad
    @field_validator('contraseña')
    def tamaño(cls, contraseña): 
        if len(contraseña) < 5: raise ValueError('La longitud mínima de la contraseña es de 5 caracteres')
        return contraseña
    @field_validator('correo')
    def validacion(cls, correo): 
        try: 
            validado = validate_email(correo)
            correo = validado.email
            return correo
        except EmailNotValidError as e: 
            raise ValueError('El email no es válido')
    
class Item(BaseModel): 
    nombre: str
    descripcion: str | None = None
    precio: float
    impuesto: float | None = None

class Producto(BaseModel): 
    Id : int
    nombre : str
    descripcio : str
    precio : float
    categoria : str
    creacion : datetime = datetime.now()
    actualizacion : datetime | None

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