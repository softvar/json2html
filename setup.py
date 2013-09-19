
import sys
from setuptools import setup

required = ['ordereddict']


if sys.version_info[:2] < (2,6):
    required.append('simplejson')

setup(
    name = 'json2html',
    packages = ['json2html'],
    version = '0.1',
    install_requires=required,
    description = 'JSON object to human readable HTML representation',
    long_description=open('README.rst').read(),
    author = 'Varun Malhotra',
    author_email = 'varun2902@gmail.com',
    url = 'https://github.com/softvar/json2html',
    download_url = 'https://github.com/softvar/json2html/tarball/0.1',
    keywords = ['json', 'HTML', 'Table'],
    license = 'MIT',
    classifiers = (
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ),
)