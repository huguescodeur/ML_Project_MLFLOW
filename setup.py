from typing import List
from setuptools import find_packages, setup


HYPEN_E_Dot='-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_Dot in requirements:
            requirements.remove(HYPEN_E_Dot)
            
    return requirements
    

setup(
    name='mlProject',
    version='0.0.1',
    author_email='goliyaohugues@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
  
)