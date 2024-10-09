from pydantic import BaseModel, EmailStr
from typing import Optional

class DataModel(BaseModel):
    nombre: str
    edad: int
    email: EmailStr
    ciudad: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "nombre": "Juan Pérez",
                "edad": 30,
                "email": "juan.perez@example.com",
                "ciudad": "Bogotá"
            }
        }
