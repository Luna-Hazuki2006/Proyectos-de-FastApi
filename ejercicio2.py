from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from datetime import *

app = FastAPI()

tiposHabitaciones = ["Individual", "Matrimonial", "Familiar"]

class reservaHotel(BaseModel):
    fechaEntrada: date
    fechaSalida: date
    numeroHuespedes: int
    tipoHabitacion: str
    '''@field_validator("fechaEntrada", "fechaSalida")
    def validarFechasReservacion(cls, fechaEntrada,fechaSalida):
        if fechaSalida <= fechaEntrada:
            raise ValueError("Fecha de salida no puede ser menor a la de entrada.")'''
    @field_validator("tipoHabitacion")
    def validarTipoHabitacion(tipoHabitacion):
        if tipoHabitacion in tiposHabitaciones:
            print("Tipo de habitación válido")
        else:
            raise ValueError("Tipo de habitación no válido.")


now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

if now < new_date:
    print("La fecha actual es menor que la nueva fecha")


fecha1 = datetime(year=2024, month=5, day=22).date()
fecha2 = datetime(year=2024, month=5, day=20).date()
if fecha1 > fecha2:
    print("Error")
reserva = reservaHotel(fechaEntrada=fecha1, fechaSalida=fecha2, numeroHuespedes="sasa", tipoHabitacion="Duplex")

print(reserva)

print("Fecha1: ", fecha1, "Fecha 2: ", fecha2)