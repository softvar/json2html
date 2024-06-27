import os, sys

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from json2html import *

_json = {
    'sample': [
        {'name': 'json2html', 'desc': 'coverts json 2 html table format', 'lang': 'python'},
        {'name': 'testing', 'desc': 'clubbing same keys of array of objects', 'lang': 'python'}
    ]
}

output = json2html.convert(json = _json)
print(output)
