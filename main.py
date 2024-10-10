from fastapi import FastAPI, Request, Form
from typing import Optional
from DataModel import DataModel 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
   return templates.TemplateResponse(request= request , name="index.html")

@app.post("/predict", response_class=HTMLResponse)
async def submit(request: Request, user_input: str = Form(...)):
   return templates.TemplateResponse(request= request, name="indexResponse.html", context={"predict": "Sexo"})



# app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}

# @app.post("/datos/")
# async def recibir_datos(datos: DataModel):
#     return {"mensaje": "Datos recibidos", "datos": datos}
