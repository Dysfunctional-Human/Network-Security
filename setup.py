"""
This setup.py file is an essential part of packaging and distributing Python projects. It is used by setuptools (or distutils in older python versions) to define the configuration of our project, such as its metadat, dependencies, and more.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """Returns the list of requirements

    Returns:
        List[str]: List containing project requirements
    """
    requirement_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # ignore the empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
        
    return requirement_list

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Aarav Kumar',
    author_email='Aarav.1197@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)