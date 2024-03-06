from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirments(file_path:str)->List[str]:
    ''' 
    This fucntion will return the list of requirements.
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
        

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Durinder',
    author_email = 'singhdurinder90@gmail.com',
    packages = find_packages(),
    #install_requires = ['pandas', 'numpy', 'seaborn']
    # As writing the name of 100s of required libraries is not feasible, we can create a function to do this task
    install_requires = get_requirments('requirements.txt')
)