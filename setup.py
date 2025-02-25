'''
Setup.py file is a essential part of packaging and distributing python projects.
It is used by setuptools (or distutils in older python versions) to define the 
configuration of your project, such as its metadata, dependancies, and more.
'''
# if __init__.py file is present in the folder, then it is considered as a package.
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function returns list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                # Ignore empty lines and -e .
                if requirement and not requirement.startswith('-e'):
                    requirement_list.append(requirement)
                    
    except FileNotFoundError:
        print('requirements.txt file not found')
        
    return requirement_list

setup(
    name="Network Security",
    version="0.0.1",
    author='Sandeep',
    author_email='sndpgauti@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
    )

                