# -*- coding: utf-8 -*-

'''
JSON 2 HTML convertor
=====================
(c) Varun Malhotra 2013
Source Code: https://github.com/softvar/json2html
Contributors:
-------------
1. Michel Müller(@muellermichel), patch #2 - https://github.com/softvar/json2html/pull/2
LICENSE: MIT
--------
'''

import json
import collections

class JSON:

	def convert(self, **args):
		'''
		convert json Object to HTML Table format
		'''

		# table attributes such as class
		# eg: table_attributes = "class = 'sortable table table-condensed table-bordered table-hover'
		global table_attributes
		table_attributes = ''

		if 'table_attributes' in args:
			table_attributes = args['table_attributes']
		else:
			# by default HTML table border
			table_attributes = 'border="1"'

		if 'json' in args:
			self.json_input = args['json']
			try:
				json.loads(self.json_input)
			except:
				self.json_input = json.dumps(self.json_input)
		else:
			raise Exception('Can\'t convert NULL!')


		ordered_json = json.loads(self.json_input, object_pairs_hook=collections.OrderedDict)

		return self.iterJson(ordered_json)


	def columnHeadersFromListOfDicts(self, ordered_json):
		'''
		If suppose some key has array of objects and all the keys are same,
		instead of creating a new row for each such entry, club those values,
		thus it makes more sense and more readable code.
		@example:
			jsonObject = {"sampleData": [ {"a":1, "b":2, "c":3}, {"a":5, "b":6, "c":7} ] }
			OUTPUT:
				<table border="1"><tr><th>1</th><td><table border="1"><tr><th>a</th><th>c</th><th>b</th></tr><tr><td>1</td><td>3</td><td>2</td></tr><tr><td>5</td><td>7</td><td>6</td></tr></table></td></tr></table>
		@contributed by: @muellermichel
		'''

		if len(ordered_json) < 2:
			return None
		if not isinstance(ordered_json[0],dict):
			return None

		column_headers = ordered_json[0].keys()

		for entry in ordered_json:
			if not isinstance(entry,dict):
				return None
			if len(entry.keys()) != len(column_headers):
				return None
			for header in column_headers:
				if not header in entry:
					return None
		return column_headers


	def iterJson(self, ordered_json):
		'''
		Iterate over the JSON and process it to generate the super awesome HTML Table format
		'''

		def markup(entry, parent_is_list = False):
			'''
			Check for each value corresponding to its key and return accordingly
			'''
			if(isinstance(entry,str)):
				return entry
			if(isinstance(entry,int) or isinstance(entry,float)):
				return str(entry)
			if(parent_is_list and isinstance(entry,list)==True):
				#list of lists are not accepted
				return ''
			if(isinstance(entry,list)==True) and len(entry) == 0:
				return ''
			if(isinstance(entry,list)==True):
				return '<ul><li>' + '</li><li>'.join([markup(child, parent_is_list=True) for child in entry]) + '</li></ul>'
			if(isinstance(entry,dict)==True):
				return self.iterJson(entry)

			#safety: don't do recursion over anything that we don't know about - iteritems() will most probably fail
			return ''

		convertedOutput = ''

		global table_attributes
		table_init_markup = "<table %s>" %(table_attributes)
		convertedOutput = convertedOutput + table_init_markup

		for k,v in ordered_json.items():
			convertedOutput = convertedOutput + '<tr>'
			convertedOutput = convertedOutput + '<th>'+ markup(k) +'</th>'

			if (v == None):
				v = ""
			if(isinstance(v,list)):
				column_headers = self.columnHeadersFromListOfDicts(v)
				if column_headers != None:
					convertedOutput = convertedOutput + '<td>'
					convertedOutput = convertedOutput + table_init_markup
					convertedOutput = convertedOutput + '<tr><th>' + '</th><th>'.join(column_headers) + '</th></tr>'
					for list_entry in v:
						convertedOutput = convertedOutput + '<tr><td>' + '</td><td>'.join([markup(list_entry[column_header]) for column_header in column_headers]) + '</td></tr>'
					convertedOutput = convertedOutput + '</table>'
					convertedOutput = convertedOutput + '</td>'
					convertedOutput = convertedOutput + '</tr>'
					continue
			convertedOutput = convertedOutput + '<td>' + markup(v) + '</td>'
			convertedOutput = convertedOutput + '</tr>'
		convertedOutput = convertedOutput + '</table>'
		return convertedOutput

json2html = JSON()
