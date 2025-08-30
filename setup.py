'''
 This setup script is used to install the package.It will handle dependencies and install the package.
 it is important to note that this script should be run in a Python environment where setuptools is installed.
 It will also handle any necessary permissions and file permissions.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function reads requirements from a file named requirements.txt and returns them as a list.
    """
    requirement_list: List[str] = []
    try:
     with open('requirements.txt', 'r') as file:
        lines=file.readlines()
        for line in lines:
          requirement = line.strip()
          if requirement and requirement!= '-e .':
             requirement_list.append(requirement)
             
    except FileNotFoundError:
       raise FileNotFoundError('The requirements file "requirements.txt" was not found.')
    return requirement_list

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Sudip',
    author_email='sudipmaji366@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)

