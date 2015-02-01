# -*- coding: utf-8 -*-

'''
JSON 2 HTML convertor
=====================

(c) Varun Malhotra 2013
Source Code: https://github.com/softvar/json2html
------------
Contributors: Michel Müller(@muellermichel), patch #2 - https://github.com/softvar/json2html/pull/2

LICENSE: MIT
--------
'''

import json
import ordereddict

a= ''

class JSON:
	#def __init__(self):

	def convert(self,**args):
		'''
		convert json Object to HTML Table format
		'''
		global table_attributes
		table_attributes = ''
		if 'table_attributes' in args:
			table_attributes = args['table_attributes']
		if 'json' in args:
			self.json_input = args['json']
			try:
				json.loads(self.json_input)
			except:
				self.json_input = json.dumps(self.json_input)
		else:
			raise Exception('Can\'t convert NULL!')


		ordered_json = json.loads(self.json_input, object_pairs_hook=ordereddict.OrderedDict)
		return self.htmlConvertor(ordered_json)

	def columnHeadersFromListOfDicts(self,ordered_json):
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

	def iterJson(self,ordered_json):
		def markupForListEntry(entry):
			if(isinstance(entry,unicode)):
				return unicode(entry)
			if(isinstance(entry,int) or isinstance(entry,float)):
				return str(entry)
			if(isinstance(entry,list)==False):
				return self.iterJson(entry)
			return ''

		global a
		global table_attributes

		table_init_markup = "<table %s>" %(table_attributes)
		a=a+ table_init_markup
		for k,v in ordered_json.iteritems():
			a=a+ '<tr>'
			a=a+ '<th>'+ str(k) +'</th>'
			if (v==None):
				v = unicode("")
			if(isinstance(v,list)):
				column_headers = self.columnHeadersFromListOfDicts(v)
				a=a+ '<td><ul>'
				if column_headers != None:
					a=a+ table_init_markup
					a=a+ '<tr><th>' + '</th><th>'.join(column_headers) + '</th></tr>'
					for list_entry in v:
						a=a+ '<tr><td>' + '</td><td>'.join([markupForListEntry(list_entry[column_header]) for column_header in column_headers]) + '</td></tr>'
					a=a+ '</table>'
				else:
					for i in range(0,len(v)):
						a=a+ '<li>'+markupForListEntry(v[i])+'</li>'
				a=a+ '</ul></td>'
				a=a+ '</tr>'
			elif(isinstance(v,unicode)):
				a=a+ '<td>'+ unicode(v) +'</td>'
				a=a+ '</tr>'
			elif(isinstance(v,int) or isinstance(v,float)):
				a=a+ '<td>'+ str(v) +'</td>'
				a=a+ '</tr>'
			else:
				a=a+ '<td>'
				#a=a+ '<table border="1">'
				self.iterJson(v)
				a=a+ '</td></tr>'
		a=a+ '</table>'

	def htmlConvertor(self,ordered_json):
		'''
		converts JSON Object into human readable HTML representation
		generating HTML table code with raw/bootstrap styling.
		'''
		global a
		a=''
		try:
			for k,v in ordered_json.iteritems():
				pass
			self.iterJson(ordered_json)
		except:
			for i in range(0,len(ordered_json)):
				if(isinstance(ordered_json[i],unicode)):
					a=a+ '<li>'+unicode(ordered_json[i])+'</li>'
				elif(isinstance(ordered_json[i],int) or isinstance(ordered_json[i],float)):
					a=a+ '<li>'+str(ordered_json[i])+'</li>'
				elif(isinstance(ordered_json[i],list)==False):
					self.htmlConvertor(ordered_json[i])

		return a


json2html = JSON()
