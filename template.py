import os
from pathlib import Path
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project base name
project_name = "streamlit"

# List of files and folders to create
list_of_files = [
    f"{project_name}/.devcontainer/devcontainer.json",
    f"{project_name}/.streamlit/config.toml",
    f"{project_name}/step1/app.py",
    f"{project_name}/README.md",
    f"{project_name}/requirements.txt",
    f"{project_name}/LICENSE"
]

# Create each file and folder
for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filename}")
