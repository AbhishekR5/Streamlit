import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Streamlit Chronicles"

# List of files to create
list_of_files = [
    f"{project_name}/.devcontainer/devcontainer.json",
    f"{project_name}/.streamlit/config.toml",
    f"{project_name}/step1/app.py",
    f"{project_name}/README.md",
    f"{project_name}/requirements.txt",
    f"{project_name}/LICENSE"
]

# Pre-fill content for important files
file_content = {
    f"{project_name}/.devcontainer/devcontainer.json": """
{
    "name": "Streamlit 30 Steps",
    "image": "mcr.microsoft.com/devcontainers/python:3.10",
    "postCreateCommand": "pip install -r requirements.txt",
    "forwardPorts": [8501],
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "ms-toolsai.jupyter"
            ]
        }
    },
    "onCreateCommand": "streamlit run step1/app.py"
}
""",

    f"{project_name}/.streamlit/config.toml": """
[theme]
base="light"
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#000000"
font="sans serif"
""",

    f"{project_name}/step1/app.py": """
import streamlit as st

st.title('🚀 Welcome to Step 1!')
st.write('Let\\'s start our 30 steps of Streamlit journey!')
""",

    f"{project_name}/requirements.txt": """
streamlit
pandas
numpy
matplotlib
plotly
altair
requests
""",

    f"{project_name}/README.md": """
# 🚀 30 Steps of Streamlit

Welcome! This repository is for practicing Streamlit daily for 30 steps.

## How to Run

- Open in GitHub Codespaces.
- It will auto-run `streamlit run step1/app.py` 🚀
- Start building your projects step-by-step!

---
Made with ❤️
""",

    f"{project_name}/LICENSE": """
MIT License
"""
}

# Create the folder and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            content = file_content.get(str(filepath), "")
            f.write(content.strip())
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")
