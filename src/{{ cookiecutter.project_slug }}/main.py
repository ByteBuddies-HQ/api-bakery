from fastapi import FastAPI
from src.{{ cookiecutter.project_slug }}.routes import main_router


# Initialize the FastAPI app
app = FastAPI()

# Register the main router
app.include_router(main_router, prefix="")

