# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='graphdb',
    version='0.0.1',
    description='Graph Database',
    long_description=long_description,
    url='https://github.com/jgraham20/graphdb',
    author='Jason Graham',
    author_email='jgraham20@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='development',
    packages=find_packages(exclude=['docs', 'tests']),
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={
        'sample': ['package_data.dat'],
    },
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
