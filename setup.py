from os.path import join, dirname
from setuptools import setup, find_packages


version = open(join(dirname(__file__), 'dysql/VERSION')).read().strip()

setup(
    name='dy-sql',
    version=version,
    license='MIT',
    description='Dynamically runs SQL queries and executions.',
    author='Ben Boger',
    author_email='***REMOVED***',
    url='https://github.com/***REMOVED***/dysql',
    platforms=['Any'],
    packages=find_packages(exclude=('*test*',)),
    zip_safe=False,
    install_requires=(
        'sqlalchemy>=1.3',
    ),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

)