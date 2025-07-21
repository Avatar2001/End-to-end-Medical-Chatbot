import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:  %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helpers.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "reasearch/trials.ipynb"
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename=os.path.split(file_path)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")

        if (not os.path.exists(filepath)or (os.path.exists(filepath) and os.path.getsize(filepath) == 0)):
            with open(filepath, 'w') as f:
                logging.info(f"Created file: {filename} in directory: {filedir}")

        else:
            logging.info(f"File {filename} already exists in directory: {filedir}") 