from setuptools import setup, find_packages

setup(
    name="sovereign-logic",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'Pillow'
    ],
    author="americosimoes",
    description="Universal SAT-to-Fluid Mapping and Zenith Satellite Reconstruction",
)
