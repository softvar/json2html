import os, sys

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from json2html import *

_json = {
    'name': 'Json2Html',
    'language':'python',
    'description': 'converts json 2 html table format'
}

output = json2html.convert(json = _json, table_attributes="class=\"table table-bordered table-hover\"")
print(output)
