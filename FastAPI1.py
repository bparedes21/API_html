from fastapi import FastAPI


app = FastAPI()

# Ruta para el formulario
@app.get("/")
async def read_form():
    return {"form.html", ""}
