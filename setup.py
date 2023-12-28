from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    
    requirements =  []
    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [i.replace('\n','') for i in requirements]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='WhatsApp Chat Analyzer',
    version='0.0.1',
    author='Karthikeya',
    author_email='karthikeyasurampudi29@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)
        