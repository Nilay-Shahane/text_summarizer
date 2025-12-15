import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = 'textSummarizer'

list_files = [
    '.github/workflow/.gitkeep', # while deploying ci/cd it will automatically deploy
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'
]

for file_path in list_files:
    file_path_two  = Path(file_path)
    print(file_path + '\t' + str(file_path_two))
    filedir , filename = os.path.split(file_path_two)
    print(filedir+'\t'+filename)

    if filedir != '':
        os.makedirs(filedir , exist_ok=True)
        logging.info(f'Creating directory : {filedir} for file {filename}')

    if (not os.path.exists(file_path_two) or os.path.getsize(file_path_two)==0):
        with open(file_path_two,'w') as f:
            pass
            logging.info(f'Creating empty file {file_path_two}')
    else :
            logging.info(f'Already exists {file_path_two}')
