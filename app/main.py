from fastapi import FastAPI
from app.routes import projects


app = FastAPI()

app.include_router(projects.router)

@app.get("/")
def read_root():
    return{"message": "Portfolio API Alisson Prado Funcionando"}