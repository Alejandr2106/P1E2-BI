from fastapi import FastAPI
from typing import Optional
from DataModel import DataModel 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola World"}

app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/datos/")
async def recibir_datos(datos: DataModel):
    return {"mensaje": "Datos recibidos", "datos": datos}
