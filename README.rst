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

1. User-friendly Table fomat - easy to read and show.
2. If any value of some key is array of objects, and all keys of all those objects are same, it will auto-club them instead of creating a new row for each Object within Array. For eg: ```jsonObject = {"sampleData": [ {"a":1, "b":2, "c":3}, {"a":5, "b":6, "c":7} ] }```
3. Easy to style for different purposes. Pass table attributes so that generated Table can have custom attributes like class, etc..


Live Demo
---------

Visit `Online json2html Convertor <http://json2html.varunmalhotra.xyz/>`_

Installation
-------------

.. code-block:: bash

	$ pip install json2html

Or, Download `here <https://github.com/softvar/json2html/tarball/0.3>`_ and run ``python setup.py install`` after changing directory to `/json2html`

Example Usage
-------------

**Example 1:** Basic usage

.. code-block:: python

	from json2html import *
	json2html.convert(json = {'name':'softvar','age':'22'})

Output:

.. code-block:: bash

	<table border="1"><tr><th>age</th><td>22</td></tr><tr><th>name</th><td>softvar</td></tr></table>

=====  =====
age    22
name   softvar
=====  =====

**Example 2:** Setting custom attributes to table

.. code-block:: python

	from json2html import *
	json2html.convert(json = {'name':'softvar','age':'22'}, table_attributes="class=\"table table-bordered table-hover\"")

Output:

.. code-block:: bash

	<table class="table table-bordered table-hover"><tr><th>age</th><td>22</td></tr><tr><th>name</th><td>softvar</td></tr></table>

**Example 3:** Clubbing same keys of: Array of Objects

.. code-block:: python

	from json2html import *
	_json2conv = {"sample": [ {"a":1, "b":2, "c":3}, {"a":5, "b":6, "c":7} ] }
	json2html.convert(json = _json2conv)

Output:

.. code-block:: bash

	<table border="1"><tr><th>sample</th><td><table border="1"><tr><th>a</th><th>c</th><th>b</th></tr><tr><td>1</td><td>3</td><td>2</td></tr><tr><td>5</td><td>7</td><td>6</td></tr></table></td></tr></table>

=====  =====  =====
a      c      b
=====  =====  =====
1      3      2
-----  -----  -----
5      7      6
=====  =====  =====

**Example 4:** Each row for different key(s) of: Array of Objects

.. code-block:: python

	from json2html import *
	_json2conv = {"sample": [ {"a":1, "b":2, "c":3}, {"1a1":5, "1b1":6, "c":7} ] }
	json2html.convert(json = _json2conv)

Output:

.. code-block:: bash

	<table border="1"><tr><th>sample</th><td><ul><li><table border="1"><tr><th>a</th><td>1</td></tr><tr><th>c</th><td>3</td></tr><tr><th>b</th><td>2</td></tr></table></li><li><table border="1"><tr><th>1b1</th><td>6</td></tr><tr><th>c</th><td>7</td></tr><tr><th>1a1</th><td>5</td></tr></table></li></ul></td></tr></table>

**Example 5:** [Source: `json.org/example <http://json.org/example>`_]

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

Tests
------

.. code-block:: bash

	cd test/
	python run_tests.py

Contributors
------------

1. Michel Müller: `@muellermichel <https://github.com/muellermichel>`_
	* `Patch #2 <https://github.com/softvar/json2html/pull/2>`_
	* Added support for clubbing Array of Objects with same keys, more readable format.
	* Added support for adding custom `table_attributes`.
	* Better error message on bad call of 'convert'

2. Daniel Lekic: `@lekic <https://github.com/lekic>`_
	* `Patch #17 <https://github.com/softvar/json2html/pull/17>`_
	* Fixed issue with one-item lists not rendering correctly.
	* General code cleanup, fixed all naming conventions and coding standards to adhere to PEP8 conventions.

Patches are highly welcomed.
