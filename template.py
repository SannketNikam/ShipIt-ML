"""
We are creating this file because we need lots of files and folders to manage our code. So instead of creating those files and folders manually we create this template.py script with some logic inside it for that so whenever we execute this file it will automatically create this file and folder structure for us.
"""

import os
from pathlib import Path
import logging

# Initializing a logging stream because we need to see the logs in the terminal
# This log some information level log with the timestamp of the code executed and the error message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s') # Logging String

# We will create a folder called src and inside that it will create mlProject 
project_name = "mlProject"

# List of files
# This will create the folders mentioned below in the current directory
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    # Before implementing our actual components we'll be doing experiments in this notebook
    "research/trials.ipynb",
    # For Flask app
    "templates/index.html"
]

# Logic to create the above folders and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)) == 0:
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty files: {filepath}")
    
    else:
        logging.info(f"{filename} already exists!")