from setuptools import setup

setup(
    name='includemd',
    version='0.0.1',
    author='Nico Hoffmann',
    author_email='n-includemd@maxdoom.com',
    packages=['includemd',],
    url='https://github.com/maxdoom-com/includemd/',
    license='LICENSE.md',
    description='A markdown extension to include markdown files from markdown files.',
    long_description=open('README.md').read(),
    install_requires=[
        'markdown',
    ],
)
