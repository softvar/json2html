json2html
=========

Python wrapper to convert ``JSON`` into a human readable ``HTML Table`` representation.

|Latest Version| |Downloads| |Build|

.. |Build| image:: https://api.travis-ci.org/softvar/json2html.png

.. |Latest Version| image:: https://img.shields.io/pypi/v/json2html.svg
    :target: https://pypi.python.org/pypi/json2html

.. |Downloads| image:: https://img.shields.io/pypi/dm/json2html.svg
        :target: https://pypi.python.org/pypi/json2html

Features
--------

* User friendly tablular fomat, easy to read and share.
* If value of the key is array of objects and all the keys are same(value of the key is a dict of list), the module will club by default. Eg.

.. code-block:: bash

	input = {
		"sampleData": [{
			"a":1, "b":2, "c":3
		}, {
			"a":5, "b":6, "c":7
		}]
	}

	will create only one row combining the results. This feature can be turned off by explicitly passing an argument ``clubbing = False``.

* Generated table can be provided some ``attributes`` explicitly. Eg. giving an ``id``, ``class`` or any ``data-*`` attribute.
* Python 3 compatible

Live Demo
----------

`Click here <http://json2html.varunmalhotra.xyz/>`_ for the online demo.

List of valid arguments
-----------------------

``json2html.convert`` - The module's ``convert`` method accepts the following arguments:

===================== ================
Argument              Description
--------------------- ----------------
`json`                a valid JSON; This can either be a string in valid JSON format or a python object that is either dict-like or list-like at the top level.
--------------------- ----------------
`table_attributes`    e.g. pass `id="info-table"` or `class="bootstrap-class"`/`data-*` to apply these attributes to the generated table
--------------------- ----------------
`clubbing`            turn on[default]/off clubbing of list with same keys of a dict / Array of objects with same key
--------------------- ----------------
`encode`              turn on/off[default] encoding of result to escaped html, compatible with any browser
--------------------- ----------------
`escape`              turn on[default]/off escaping of html tags in text nodes (prevents XSS attacks in case you pass untrusted data to json2html)
===================== ================

Installation
------------

.. code-block:: bash

	$ pip install json2html

Or, Download [here](https://github.com/softvar/json2html/releases) and run `python setup.py install` after changing directory to `/json2html`

Example Usage
-------------

**Example 1:** Basic usage

.. code-block:: python

	from json2html import *
	input = {
		"name": "json2html",
		"description": "Converts JSON to HTML tabular representation"
	}
	json2html.convert(json = input)

Output:

.. code-block:: bash

	<table border="1"><tr><th>name</th><td>json2html</td></tr><tr><th>description</th><td>converts JSON to HTML tabular representation</td></tr></table>

============ ========================================================
name         json2html
------------ --------------------------------------------------------
description  Converts JSON to HTML tabular representation
============ ========================================================

**Example 2:** Setting custom attributes to table

.. code-block:: python

	from json2html import *
	input = {
		"name": "json2html",
		"description": "Converts JSON to HTML tabular representation"
	}
	json2html.convert(json = input, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")

Output:

.. code-block:: bash

	<table id="info-table" class="table table-bordered table-hover"><tr><th>name</th><td>json2html</td></tr><tr><th>description</th><td>Converts JSON to HTML tabular representation</td></tr></table>

**Example 3:** Clubbing same keys of: Array of Objects

.. code-block:: python

	from json2html import *
	input = {
		"sample": [{
			"a":1, "b":2, "c":3
		}, {
			"a":5, "b":6, "c":7
		}]
	}
	json2html.convert(json = input)

Output:

.. code-block:: bash

	<table border="1"><tr><th>sample</th><td><table border="1"><thead><tr><th>b</th><th>c</th><th>a</th></tr></thead><tbody><tr><td>2</td><td>3</td><td>1</td></tr><tr><td>6</td><td>7</td><td>5</td></tr></tbody></table></td></tr></table>

======== ======= =======
  a         c      b
-------- ------- -------
   1        3       2
-------- ------- -------
   5        7       6
======== ======= =======

**Example 4:** Each row for different key(s) of: Array of Objects

.. code-block:: python

	from json2html import *
	input = {
		"sample": [{
			"a":1, "b":2, "c":3
		}, {
			"1a1":5, "1b1":6, "c":7
		}]
	}
	json2html.convert(json = input)

Output:

.. code-block:: bash

	<table border="1"><tr><th>sample</th><td><ul><li><table border="1"><tr><th>a</th><td>1</td></tr><tr><th>c</th><td>3</td></tr><tr><th>b</th><td>2</td></tr></table></li><li><table border="1"><tr><th>1b1</th><td>6</td></tr><tr><th>c</th><td>7</td></tr><tr><th>1a1</th><td>5</td></tr></table></li></ul></td></tr></table>

**Example 5:** [Source: `json.org/example <http://json.org/example>`_]

.. code-block:: python

	from json2html import *

	input = {
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

	json2html.convert(json = input)

Output:

.. code-block:: bash

	<table border="1"><tr><th>glossary</th><td><table border="1"><tr><th>GlossDiv</th><td><table border="1"><tr><th>GlossList</th><td><table border="1"><tr><th>GlossEntry</th><td><table border="1"><tr><th>GlossDef</th><td><table border="1"><tr><th>GlossSeeAlso</th><td><ul><li>GML</li><li>XML</li></ul></td></tr><tr><th>para</th><td>A meta-markup language, used to create markup languages such as DocBook.</td></tr></table></td></tr><tr><th>GlossSee</th><td>markup</td></tr><tr><th>Acronym</th><td>SGML</td></tr><tr><th>GlossTerm</th><td>Standard Generalized Markup Language</td></tr><tr><th>Abbrev</th><td>ISO 8879:1986</td></tr><tr><th>SortAs</th><td>SGML</td></tr><tr><th>ID</th><td>SGML</td></tr></table></td></tr></table></td></tr><tr><th>title</th><td>S</td></tr></table></td></tr><tr><th>title</th><td>example glossary</td></tr></table></td></tr></table>

Tests
------

.. code-block:: bash

	cd test/
	python run_tests.py

Tested with Python 2.6, 2.7 3.4, and 3.5.

Contributors
------------

1. Michel Mueller: [@muellermichel](https://github.com/muellermichel)
	* Added support for clubbing Array of Objects with same keys, more readable format.
	* Added support for adding custom `table_attributes`.
	* Convert now accepts unicode and bytestrings for the keyword argument "json".
	* Output now should always appear in the same order as input.
	* Now supports JSON Lists (at top level), including clubbing.
	* Now supports empty inputs and positional arguments for convert.
	* Python 3 support ; Added integration tests for Python 2.6, 3.4 and 3.5 such that support doesn't break.
	* Can now also do the proper encoding for you (disabled by default to not break backwards compatibility).
	* Can now handle non-JSON objects on a best-effort principle.
	* Now by default escapes html in text nodes to prevent XSS attacks.

2. Daniel Lekic: [@lekic](https://github.com/lekic)
	* Fixed issue with one-item lists not rendering correctly.
	* General code cleanup, fixed all naming conventions and coding standards to adhere to PEP8 conventions.

3. Kyle Smith: [@smithk86](https://github.com/smithk86)
    * Added thead and tbody tags to group header and content rows when creating a table from an array of objects.

Copyright and License
---------------------

	The `MIT license <https://opensource.org/licenses/MIT>`_

	Copyright (c) 2014-2017 Varun Malhotra

	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
