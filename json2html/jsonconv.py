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
    import simplejson as json
else:
    import json


class Json2Html:

    def convert(self, **kwargs):
        """
            Convert JSON to HTML Table format
        """

        # table attributes such as class, id, data-attr-*, etc.
        # eg: table_attributes = 'class = "table table-bordered sortable"'
        global table_attributes
        table_attributes = ''

        if 'table_attributes' in kwargs:
            table_attributes = kwargs['table_attributes']
        else:
            # by default HTML table border
            table_attributes = 'border="1"'

        if 'json' in kwargs and kwargs['json']:
            self.json_input = kwargs['json']
            try:
                json.loads(self.json_input)
            except:
                self.json_input = json.dumps(self.json_input)
        else:
            raise Exception("Please use json2html's convert function with a keyword argument 'json' - e.g. `json2html.convert(json={\"hello\":\"world!\"})`")

        inputted_json = json.loads(self.json_input)
        return self.iter_json(inputted_json)

    def column_headers_from_list_of_dicts(self, inputted_json):
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

        if not inputted_json or not isinstance(inputted_json[0], dict):
            return None

        column_headers = inputted_json[0].keys()

        for entry in inputted_json:
            if not isinstance(entry, dict) or (len(entry.keys()) != len(column_headers)):
                return None
            for header in column_headers:
                if header not in entry:
                    return None
        return column_headers

    def iter_json(self, inputted_json):
        """
            Iterate over the JSON and process it
            to generate the super awesome HTML Table format
        """

        def markup(entry):
            """
                Check for each value corresponding to its key
                and return accordingly
            """
            if isinstance(entry, unicode):
                return unicode(entry)
            if isinstance(entry, int) or isinstance(entry, float):
                return str(entry)
            if isinstance(entry, list) and len(entry) == 0:
                return ''
            if isinstance(entry, list):
                list_markup = '<ul><li>'
                list_markup += '</li><li>'.join([markup(child) for child in entry])
                list_markup += '</li></ul>'
                return list_markup
            if isinstance(entry, dict):
                return self.iter_json(entry)

            # safety: don't do recursion over anything that we don't know about
            # - iteritems() will most probably fail
            return ''

        converted_output = ''

        global table_attributes
        table_init_markup = "<table %s>" % table_attributes
        converted_output += table_init_markup

        try:
            for (k, v) in inputted_json.iteritems():
                converted_output += '<tr><th>' + markup(k) + '</th>'

                if v is None:
                    v = unicode("")
                if isinstance(v, list):
                    column_headers = self.column_headers_from_list_of_dicts(v)
                    if column_headers is not None:
                        converted_output += '<td>'
                        converted_output += table_init_markup
                        converted_output += '<tr><th>' + '</th><th>'.join(column_headers) + '</th></tr>'
                        for list_entry in v:
                            converted_output += '<tr><td>'
                            converted_output += '</td><td>'.join([markup(list_entry[column_header]) for column_header in
                                                                 column_headers])
                            converted_output += '</td></tr>'

                        converted_output += '</table></td></tr>'
                        continue
                converted_output += '<td>' + markup(v) + '</td></tr>'
            converted_output += '</table>'

        except:
            raise Exception('Not a valid JSON list')
        return converted_output

json2html = Json2Html()
