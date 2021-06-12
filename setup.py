# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()

with open('.version', 'r') as f:
    version = f.read().split('=')[1]

setup(
    name='pytest-skipslow',
    description='A Pytest plugin to ignore slow tests by default',
    author='Natalia Maximo',
    author_email='iam@natalia.dev',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/taliamax/pytest-skipslow',
    license='MIT License',
    packages=find_packages('src'),
    extras_require={
        'tests': ['flake8', 'mypy'],
    },
    package_dir={'': 'src'},
    include_package_data=True,
    version=version,
    install_requires=[
        'pytest'
    ],
    python_requires='>=3.6',
    keywords=['pytest', 'plugin'],
    entry_points={
        'pytest11': [
            'pytest_skipslow = pytest_skipslow',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Pytest',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)
