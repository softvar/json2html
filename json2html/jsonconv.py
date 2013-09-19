import json
import ordereddict

class JSON:
	#def __init__(self):

	def convert(self,**args):
		'''
		convert json Object to HTML Table format
		'''
		if 'json' in args:
			self.json_input = args['json']
			self.json_input = json.dumps(self.json_input)
		else:
			raise Exception('Can\'t convert NULL!')
		

		ordered_json = json.loads(self.json_input, object_pairs_hook=ordereddict.OrderedDict)
		self.htmlConvertor(ordered_json)

	def htmlConvertor(self,ordered_json):
		for k,v in ordered_json.iteritems():
			print '<tr>'
			print '<th>'+ str(k) +'</th>'
			if(isinstance(v,list)):
				print '<td><ul>'
				for i in range(0,len(v)):
					print '<li>'+str(v[i])+'</li>'
				print '</ul></td>'
				print '</tr>'
			elif(isinstance(v,unicode)):
				print '<td>'+ str(v) +'</td>'
				print '</tr>'
			else:
				print '<td>'
				print '<table border="1">'
				self.htmlConvertor(v)
				print '</table></td>'

#j = JSON()
#j.convert(json = {'1':'a','2':'b'})
json2html = JSON()