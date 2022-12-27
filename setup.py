from setuptools import find_packages, setup
from typing import List


REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements_list = requirement_file.readlines()
        requirements_list = [requirement_name.replace("\n", "") for requirement_name in requirements_list]
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)

    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="Mathujan Sivananthan",
    author_email="smathujan03@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)