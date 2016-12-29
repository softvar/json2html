# -*- coding: utf-8 -*-

"""
JSON 2 HTML Converter
=====================

(c) Varun Malhotra 2013
Source Code: https://github.com/softvar/json2html


Contributors:
-------------
1. Michel Müller (@muellermichel), https://github.com/softvar/json2html/pull/2
2. Daniel Lekic (@lekic), https://github.com/softvar/json2html/pull/17

LICENSE: MIT
--------
"""

import sys

if sys.version_info[:2] < (2, 7):
    from ordereddict import OrderedDict
    import simplejson as json
else:
    from collections import OrderedDict
    import json

if sys.version_info[:2] < (3, 0):
    text = unicode
    text_types = [unicode, str]
else:
    text = str
    text_types = [str]

class Json2Html:

    def convert(self, **kwargs):
        """
            Convert JSON to HTML Table format
        """

        # table attributes such as class, id, data-attr-*, etc.
        # eg: table_attributes = 'class = "table table-bordered sortable"'
        table_attributes = None
        if 'table_attributes' in kwargs:
            table_attributes = kwargs['table_attributes']
        else:
            # by default HTML table border
            table_attributes = 'border="1"'
        self.table_init_markup = "<table %s>" % table_attributes

        json_input = None
        if 'json' in kwargs and kwargs['json']:
            unvalidated_input = kwargs['json']
            if type(unvalidated_input) in text_types:
                json_input = json.loads(unvalidated_input, object_pairs_hook=OrderedDict)
            else:
                json_input = unvalidated_input
        else:
            raise ValueError("Please use json2html's convert function with a keyword argument 'json' - e.g. `json2html.convert(json={\"hello\":\"world!\"})`")

        if isinstance(json_input, list):
            return self.convert_list(json_input)
        return self.convert_json(json_input)

    def column_headers_from_list_of_dicts(self, json_input):
        """
            If suppose some key has array of objects and all the keys are same,
            instead of creating a new row for each such entry,
            club such values, thus it makes more sense and more readable table.

            @example:
                jsonObject = {
                    "sampleData": [
                        {"a":1, "b":2, "c":3},
                        {"a":5, "b":6, "c":7}
                    ]
                }
                OUTPUT:
                _____________________________
                |               |   |   |   |
                |               | a | c | b |
                |   sampleData  |---|---|---|
                |               | 1 | 3 | 2 |
                |               | 5 | 7 | 6 |
                -----------------------------

            @contributed by: @muellermichel
        """
        if not json_input or not isinstance(json_input[0], dict):
            return None

        column_headers = json_input[0].keys()
        for entry in json_input:
            if not isinstance(entry, dict) or (len(entry.keys()) != len(column_headers)):
                return None
            for header in column_headers:
                if header not in entry:
                    return None
        return column_headers

    def convert_json(self, json_input):
        """
            Iterate over the JSON input and process it
            to generate the super awesome HTML format
        """
        if type(json_input) in text_types:
            return text(json_input)
        if isinstance(json_input, int) or isinstance(json_input, float):
            return str(json_input)
        if isinstance(json_input, list) and len(json_input) == 0:
            return ''
        if isinstance(json_input, list):
            list_markup = '<ul><li>'
            list_markup += '</li><li>'.join([self.convert_json(child) for child in json_input])
            list_markup += '</li></ul>'
            return list_markup
        if isinstance(json_input, dict):
            return self.convert_object(json_input)

        # safety: don't do recursion over anything that we don't know about
        # - iteritems() will most probably fail
        return ''

    def convert_list(self, list_input):
        """
            Iterate over the JSON list and process it
            to generate either an HTML table or a HTML list, depending on what's inside.
        """
        converted_output = ""
        column_headers = self.column_headers_from_list_of_dicts(list_input)
        if column_headers is not None:
            converted_output += self.table_init_markup
            converted_output += '<tr><th>' + '</th><th>'.join(column_headers) + '</th></tr>'
            for list_entry in list_input:
                converted_output += '<tr><td>'
                converted_output += '</td><td>'.join([self.convert_json(list_entry[column_header]) for column_header in
                                                     column_headers])
                converted_output += '</td></tr>'
            converted_output += '</table>'
        else:
            converted_output += self.convert_json(list_input)
        return converted_output

    def convert_cell_content(self, cell_input):
        """
            Wrap content in <td> markup
        """
        return '<td>' + self.convert_json(cell_input) + '</td>'

    def convert_object(self, json_input):
        """
            Iterate over the JSON object and process it
            to generate the super awesome HTML Table format
        """
        converted_output = self.table_init_markup
        for k, v in json_input.items():
            converted_output += '<tr><th>' + self.convert_json(k) + '</th>'
            if v is None:
                v = text("")
            if isinstance(v, list):
                converted_output += self.convert_cell_content(self.convert_list(v)) + "</tr>"
            else:
                converted_output += self.convert_cell_content(v) + "</tr>"
        converted_output += '</table>'
        return converted_output

json2html = Json2Html()
