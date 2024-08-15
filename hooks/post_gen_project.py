import subprocess


def run():
    """Automatically install Poetry, project dependencies, and set up pre-commit hooks."""
    # Install poetry dependencies
    subprocess.run(["poetry", "install"], check=True)
    
    # Install pre-commit hooks
    subprocess.run(["poetry", "run", "pre-commit", "install"], check=True)

if __name__ == "__main__":
    run()
