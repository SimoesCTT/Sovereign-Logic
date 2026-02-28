from setuptools import setup, find_packages

setup(
    name='sovereign-logic',
    version='1.1.0',
    packages=find_packages(),
    install_requires=['numpy'],
    author='Americo Simoes',
    description='1024-bit Unitary Lattice and Sovereign Logic Bridge',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SimoesCTT/Sovereign-Logic',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
