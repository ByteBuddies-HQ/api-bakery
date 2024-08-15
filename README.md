# API Bakery
cookie cutter template for API projects


## Structure

api-bakery/
│
├── cookiecutter.json
├── {{ cookiecutter.project_slug }}/
│   ├── pyproject.toml         # Poetry configuration
│   ├── README.md              # Project documentation
│   ├── .gitignore             # Standard gitignore file
│   ├── src/                   # Source code for FastAPI project
│   │   └── {{ cookiecutter.project_slug }}/
│   │       ├── __init__.py
│   │       └── main.py        # FastAPI app entry point
│   ├── tests/                 # Unit tests folder
│   │   └── test_main.py
│   ├── local_data/            # Folder for local data
│   └── .env                   # Optional environment configuration
└── hooks/
    └── post_gen_project.py     # Install Poetry and dependencies after project generation

