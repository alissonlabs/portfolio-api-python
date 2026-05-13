from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException
from app.database.memory_db import projects, next_id

router = APIRouter()

# banco em memória (temporário)
projects = []
next_id = 1

# 📦 Modelo de dados (entrada da API)
class Project(BaseModel):
    title: str
    description: str

# GET - Listar Projetos
@router.get("/projects")
def get_projects():
    return projects

# POST - Criar Projetos
@router.post("/projects")
def create_projects(project: Project):
    global next_id

    new_project = {
        "id" : next_id,
        "title": project.title,
        "description" : project.description
    }

    projects.append(new_project)
    next_id += 1

    return new_project

# Percorre a lista e retorna o Id solicitado
@router.get("/projects/{project_id}")
def get_project_by_id(project_id: int):
    for project in projects:
        if project["id"]== project_id:
            return project
        
    return{"error": "Projeto nao encontrado"}
        

# Em busca do CRUD --> Delete
@router.delete("/projects/{project_id}")
def delete_project(project_id: int):
    for index, project in enumerate(projects):
        if project["id"] == project_id:
            deleted = projects.pop(index)
            return {
                "message" : "Projeto removido com sucesso",
                "project" : deleted

            }
        
    return {"error" : "Projeto nao Encontrado"}
    
# Endpoint de Atualizacao PUT 
@router.put("/projects/{projects_id}")
def update_project(project_id: int, project: Project):
    for p in projects:
        if p["id"] == project_id:
            p.update(project.model_dump())
            return p
        
    raise HTTPException(status_code=404, detail="Projeto nao encontrado")
    