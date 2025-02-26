from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath: str) -> List[str]:
    """Read the requirements file and return a list of dependencies."""
    requirements = []
    with open(filepath, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]  # Use strip() to clean spaces/newlines

    # Remove '-e .' if present (fix indentation)
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements  # ✅ Return list correctly

setup(
    name='MLP',
    version='0.0.1',
    author='Oscar Owino',
    author_email='owino4011@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
