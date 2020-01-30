from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='HOTT',
    version='0.1',
    url='https://github.com/lambdaofgod/HOTT',
    packages=find_packages(),
    install_requires=requirements
)
