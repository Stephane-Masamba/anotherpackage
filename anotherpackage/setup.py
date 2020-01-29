from setuptools import setup, find_packages

setup(
    name='anotherpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    url='https://github.com/stephane-masamba/anotherpackage',
    author='stephane masamba',
    author_email='sm.masamba@gmail.com'
    )