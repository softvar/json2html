from setuptools import setup

setup(
    name = 'json2html',
    packages = ['json2html'],
    version = '1.3.0',
    description = 'JSON to HTML Table Representation',
    long_description=open('README.md').read(),
    author = 'Varun Malhotra',
    author_email = 'varun2902@gmail.com',
    url = 'https://github.com/softvar/json2html',
    download_url = 'https://github.com/softvar/json2html/tarball/1.3.0',
    keywords = ['json', 'HTML', 'Table'],
    license = 'MIT',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
