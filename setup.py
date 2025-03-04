from typing import List
from setuptools import setup, find_packages

def get_requirements() -> List[str]:
    """
    Reads the 'requirements.txt' file and returns a list of dependencies
    to be included in the 'install_requires' parameter of the setup function.

    This function opens 'requirements.txt', reads its contents, and parses
    each line to extract the dependencies. Lines that are empty or contain
    only the editable install marker ('-e .') are ignored.

    Returns:
        List[str]: A list of strings representing the package dependencies.

    Raises:
        FileNotFoundError: If 'requirements.txt' does not exist in the current directory.
    """
    requirements_list: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirements_list

setup(
    name="Resume-Parser",
    author='Gujuri Alekha',
    author_email='gujurialekha@gmail.com',
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements()
)
