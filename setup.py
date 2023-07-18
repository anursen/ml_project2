from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."

file_path = r"requirements.txt"


def get_requirements():
    """
    This function will return the list of reuqirements
    """
    requirements = []
    with open(file_path,encoding="utf-8")) as file:
        requirements = file.readlines()
        requirements = [required.replace("\n", "") for required in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="ml_project2",
    version="1.0",
    description="End to end ml project",
    author="Abdurrahim Nursen",
    author_email="anurse007@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(file_path),
)
