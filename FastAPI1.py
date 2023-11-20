from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from databases import Database

app = FastAPI()


# Configuración de plantillas Jinja2
templates = Jinja2Templates(directory="templates")
# Ruta para el formulario
@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Ruta para procesar el formulario
@app.post("/submit/")
async def submit_form(request: Request, title: str = Form(...), content: str = Form(...)):
    # Conexión a la base de datos


    return templates.TemplateResponse("submitted.html", {"request": request, "title": title, "content": content})
