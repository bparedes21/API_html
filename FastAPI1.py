from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from databases import Database

app = FastAPI()

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)

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
    database.connect()

    # Crear una tabla si no existe
    database.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT
        )
        """
    )

    # Insertar datos en la tabla
    database.execute("INSERT INTO notes (title, content) VALUES (:title, :content)", values={"title": title, "content": content})

    # Desconectar de la base de datos
    database.disconnect()

    return templates.TemplateResponse("submitted.html", {"request": request, "title": title, "content": content})

@app.get("/show_data/")
async def show_data(request: Request):
    # Conexión a la base de datos
    database.connect()

    # Crear una tabla si no existe
    # Fetch multiple rows
    query = "SELECT * FROM notes"
    rows = database.fetch_all(query=query)
    # Desconectar de la base de datos
    database.disconnect()
    return templates.TemplateResponse("show_data.html", {"request": request, "data": rows})
# Nueva ruta para redirigir a la página que muestra todos los datos
@app.get("/all_data/")
async def all_data(request: Request):
    return templates.TemplateResponse("show_data.html", {"request": request})