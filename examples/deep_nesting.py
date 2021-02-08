import os, sys

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from json2html import *

_json = {
        "glossary": {
                "title": "example glossary",
                "GlossDiv": {
                        "title": "S",
                        "GlossList": {
                                "GlossEntry": {
                                        "ID": "SGML",
                                        "SortAs": "SGML",
                                        "GlossTerm": "Standard Generalized Markup Language",
                                        "Acronym": "SGML",
                                        "Abbrev": "ISO 8879:1986",
                                        "GlossDef": {
                                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                                "GlossSeeAlso": ["GML", "XML"]
                                        },
                                        "GlossSee": "markup"
                                }
                        }
                }
        }
}

output = json2html.convert(json = _json)
print(output)
