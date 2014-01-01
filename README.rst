json2html
=========

Python wrapper to convert ``JSON object`` into a human readable ``HTML`` representation.

Features
--------

1. User-friendly readable format.
2. Easy to style for different purposes.

Installation
-------------

.. code-block:: bash

    $ pip install json2html

Or, Download `here <https://github.com/softvar/json2html/tarball/0.1>`_ and run ``python setup.py install`` after changing directory to `/json2html`

Example Usage
-------------

Example 1:

.. code-block:: python

    from json2html import *
    json2html.convert(json = {'name':'softvar','age':'21'})

Output:

.. code-block:: bash 

    <table border="1"><tr><th>age</th><td>21</td></tr><tr><th>name</th><td>softvar</td></tr></table>

Example 2: [Source: `json.org/example <http://json.org/example>`_]

.. code-block:: python

    from json2html import *

    _json2conv = {
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
    
    json2html.convert(json = _json2conv)

Output:

.. code-block:: bash

    <table border="1"><tr><th>glossary</th><td><table border="1"><tr><th>GlossDiv</th><td><table border="1"><tr><th>GlossList</th><td><table border="1"><tr><th>GlossEntry</th><td><table border="1"><tr><th>GlossDef</th><td><table border="1"><tr><th>GlossSeeAlso</th><td><ul><li>GML</li><li>XML</li></ul></td></tr><tr><th>para</th><td>A meta-markup language, used to create markup languages such as DocBook.</td></tr></table></td></tr><tr><th>GlossSee</th><td>markup</td></tr><tr><th>Acronym</th><td>SGML</td></tr><tr><th>GlossTerm</th><td>Standard Generalized Markup Language</td></tr><tr><th>Abbrev</th><td>ISO 8879:1986</td></tr><tr><th>SortAs</th><td>SGML</td></tr><tr><th>ID</th><td>SGML</td></tr></table></td></tr></table></td></tr><tr><th>title</th><td>S</td></tr></table></td></tr><tr><th>title</th><td>example glossary</td></tr></table></td></tr></table>

Live Demo
---------

Visit `json2html Convertor <http://json2html.herokuapp.com>`_






