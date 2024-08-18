from fastapi import APIRouter


main_router = APIRouter()

@main_router.get("/")
async def root():
    return {"message": "Welcome to {{ cookiecutter.project_name }}!"}

@main_router.get("/status")
async def status():
    return {"status": "API is running smoothly"}
