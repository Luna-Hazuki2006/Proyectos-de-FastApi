from pydantic import BaseModel

class ItemBase(BaseModel): 
    titulo : str
    descripcion : str | None = None

class ItemCreado(ItemBase): 
    pass

class Item(ItemBase): 
    id : int
    id_dueño : int

    class Configuracion: 
        modo_orm = True

class UsuarioBase(BaseModel): 
    correo : str

class UsuarioCreado(UsuarioBase): 
    contraseña : str

