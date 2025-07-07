# setup.py
# This file is used for packaging and distributing the NetworkSecurity project.
# It defines metadata, dependencies, and configuration for the project.

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements from a file and returns a list of dependencies.
    
    Args:
        file_path (str): Path to the requirements file.
    
    Returns:
        List[str]: A list of package names.
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines = file.readlines()
            #Process lines to remove comments and empty lines
            
            for line in lines:
                requirements = line.strip() 
                if requirements and requirements != '-e .':
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
    
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Abhinav Bhasker',
    author_email='abbhaske@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements()
    )
