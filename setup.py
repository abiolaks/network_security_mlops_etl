"""
The setup.py file is an ensential part of packaging and distributiing
python projects. It is used by setuptools to define the configuration of your project
, such as its metadata, dependencies, and scripts.
"""

from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements.txt file and returns a list of requirements
    """
    requirements_lst: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            # readlines from the files
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirements_lst


#print(get_requirements("requirements.txt"))

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Kingsley Lawani",
    packages=find_packages(),
    install_requires=get_requirements()
)
