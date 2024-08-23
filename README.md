<div align="center">

   ![Python Badge](https://img.shields.io/badge/-Python-3B4252?style=flat&logo=python&logoColor=EBCB8B)
  
</div>

<br>

# This is the API bakery...
> a cookiecutter template

This template helps generate FastAPI project structures quickly and consistently across this team. It sets up a baseline structure, along with testing, linting, and version control configurations. Below is a guide to get started with this template.

For more info: [read the docs](https://cookiecutter.readthedocs.io/en/stable/)

<br>

## Table of Contents
1. [Features](#features)
2. [Folder Structure](#folder-structure)
3. [How to Use This Template](#how-to-use-this-template)
4. [Project Setup Steps](#project-setup-steps)
5. [How to Run the Application](#how-to-run-the-application)
6. [Testing](#testing)
7. [Linting & Code Quality](#linting--code-quality)
8. [Contributing](#contributing)

---

## Features
This template includes:
- Basic FastAPI application setup.
- A modular project structure for easy scalability.
- Pre-configured linting, and code consistence using `pre-commit` hooks.
- Example unit tests using `pytest`.
- Automatic `post_gen_project` hooks for smooth setup.
- Pre-configured `pyproject.toml` for dependency management and build tools.


## Folder Structure

Once you use the template, the generated FastAPI project will follow this folder structure:

```
{{ cookiecutter.project_slug }}/
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── .gitignore                 
├── pyproject.toml              # Project dependencies and configuration
├── README.md                   # Project-specific documentation
├── src/                        # Application source code
│   ├── {{ cookiecutter.project_slug }}/  
│   │   ├── __init__.py         
│   │   ├── main.py             # Entry point for the FastAPI app
│   │   └── routes.py           # API routes configuration
├── tests/                      # Testing framework
│   └── test_main.py            # Example unit test for main FastAPI app
└── hooks/
    └── post_gen_project.py      # Post-cookiecutter generation actions
```


## How to Use This Template

### Prerequisites
- Python 3.8+
- Cookiecutter installed (`pip install cookiecutter`)

### Installation

To use this cookiecutter template, follow these steps:

1. Ensure `cookiecutter` is installed:
    ```bash
    pip install cookiecutter
    ```

2. Clone or reference this repository URL when using `cookiecutter`:
    ```bash
    cookiecutter https://github.com/ByteBuddies-HQ/api-bakery
    ```

3. You will be prompted to provide values for the following:
    - `project_name`: Name of your project.
    - `project_slug`: The folder name for your project (lowercase, no spaces).
    - `author_name`: Your name or team name.
    - `version`: The initial version of your project.



Answer the prompts as follows:
```text
project_name [My FastAPI Project]: <project name>
project_slug [api_bakery]: <project_name>
author_name [Your Name]: <your_name>
version [0.0.1]: <version number>
```


## Project Setup Steps

After running cookiecutter, follow these steps:

1. Navigate to the generated project folder:
    ```bash
    cd <your_project>
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r environment.yaml
    ```

4. (Optional) Initialize git if not already done:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

5. Install pre-commit hooks:
    ```bash
    pre-commit install
    ```

6. Run the post-generation hook to finalize setup (if not automatically triggered):
    ```bash
    python hooks/post_gen_project.py
    ```


## How to Run the Application

Once the environment is set up, you can run the FastAPI app using the following command:

1. **Running locally**:
    ```bash
    uvicorn src.main:app --reload
    ```

    The application should now be accessible at `http://127.0.0.1:8000`.

2. **API Documentation**:
    FastAPI automatically provides two types of documentation:
    - OpenAPI docs: `http://127.0.0.1:8000/docs`
    - Alternative Swagger UI: `http://127.0.0.1:8000/redoc`


## Testing

This project comes with an example test configuration using `pytest`. You can run the tests with:

```bash
pytest
```

You can add more tests inside the `tests/` folder to validate the functionality of your application.


## Linting & Code Quality

To ensure code quality, this template includes `pre-commit` hooks. They automatically check your code for style and common errors before allowing commits.

To run the checks manually:
```bash
pre-commit run --all-files
```

## Contributing

If you wish to contribute to improving this template, follow these steps:

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m "Add x feature"`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request
