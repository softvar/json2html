# -*- coding: utf-8 -*-

'''
JSON 2 HTML convertor
=====================

(c) Varun Malhotra 2013
Source Code: https://github.com/softvar/json2html


Contributors:
-------------
1. Michel Müller(@muellermichel), https://github.com/softvar/json2html/pull/2

LICENSE: MIT
--------
'''

import sys

if (sys.version_info[:2] < (2, 7)):
    import simplejson as json
else:
    import json


class Json2Html:

    def convert(self, *args, **kwargs):
        '''
            Convert JSON to HTML Table format
        '''

        # table attributes such as class, id, data-attr-*, etc.
        # eg:
        # table_attributes = 'class = "table table-bordered sortable"'
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

        inputtedJson = json.loads(self.json_input)
        return self.iterJson(inputtedJson)

    def columnHeadersFromListOfDicts(self, inputtedJson):
        '''
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
        '''

        if len(inputtedJson) < 2:
            return None
        if not isinstance(inputtedJson[0], dict):
            return None

        column_headers = inputtedJson[0].keys()

        for entry in inputtedJson:
            if not isinstance(entry, dict):
                return None
            if len(entry.keys()) != len(column_headers):
                return None
            for header in column_headers:
                if header not in entry:
                    return None
        return column_headers

    def iterJson(self, inputtedJson):
        '''
            Iterate over the JSON and process it
            to generate the super awesome HTML Table format
        '''

        def markup(entry):
            '''
                Check for each value corresponding to its key
                and return accordingly
            '''
            if (isinstance(entry, unicode)):
                return unicode(entry)
            if (isinstance(entry, int) or isinstance(entry, float)):
                return str(entry)
            if (isinstance(entry, list) == True) and len(entry) == 0:
                return ''
            if (isinstance(entry, list) == True):
                listMarkup = ''
                listMarkup += '<ul><li>'
                listMarkup += '</li><li>'.join([markup(child) for child in entry])
                listMarkup += '</li></ul>'
                return listMarkup
            if (isinstance(entry, dict) == True):
                return self.iterJson(entry)

            # safety: don't do recursion over anything that we don't know about
            # - iteritems() will most probably fail
            return ''

        convertedOutput = ''

        global table_attributes
        table_init_markup = "<table %s>" % (table_attributes)
        convertedOutput = convertedOutput + table_init_markup

        try:
            for (k, v) in inputtedJson.iteritems():
                convertedOutput = convertedOutput + '<tr>'
                convertedOutput = convertedOutput + '<th>' + markup(k) + '</th>'

                if (v is None):
                    v = unicode("")
                if(isinstance(v, list)):
                    column_headers = self.columnHeadersFromListOfDicts(v)
                    if column_headers is not None:
                        convertedOutput = convertedOutput + '<td>'
                        convertedOutput += table_init_markup
                        convertedOutput += '<tr><th>' + '</th><th>'.join(column_headers) + '</th></tr>'
                        for list_entry in v:
                            convertedOutput = convertedOutput
                            convertedOutput += '<tr><td>'
                            convertedOutput += '</td><td>'.join([markup(list_entry[column_header]) for column_header in column_headers])
                            convertedOutput += '</td></tr>'

                        convertedOutput = convertedOutput + '</table></td></tr>'
                        continue
                convertedOutput = convertedOutput + '<td>' + markup(v) + '</td>'
                convertedOutput = convertedOutput + '</tr>'
            convertedOutput = convertedOutput + '</table>'

        except:
            raise Exception('Not a valid JSON list')
        return convertedOutput

json2html = Json2Html()
