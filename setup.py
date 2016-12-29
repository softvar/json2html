import sys
from setuptools import setup

required = []


if sys.version_info[:2] < (2,7):
    required.append('simplejson')
    required.append('ordereddict')

setup(
    name = 'json2html',
    packages = ['json2html'],
    version = '1.1.0',
    install_requires=required,
    description = 'JSON to HTML Table Representation',
    long_description=open('README.md').read(),
    author = 'Varun Malhotra',
    author_email = 'varun2902@gmail.com',
    url = 'https://github.com/softvar/json2html',
    download_url = 'https://github.com/softvar/json2html/tarball/1.1.0',
    keywords = ['json', 'HTML', 'Table'],
    license = 'MIT',
    classifiers = (
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ),
)
