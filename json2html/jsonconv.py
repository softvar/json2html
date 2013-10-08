import json
import ordereddict

a= ''

class JSON:
	#def __init__(self):

	def convert(self,**args):
		'''
		convert json Object to HTML Table format
		'''
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

	def htmlConvertor1(self,ordered_json):
		print '<table border="1">'
		for k,v in ordered_json.iteritems():
			print '<tr>'
			print '<th>'+ str(k) +'</th>'
			if(isinstance(v,list)):
				print '<td><ul>'
				for i in range(0,len(v)):
					if(isinstance(v[i],unicode)):
						a=a+ '<li>'+str(v[i])+'</li>'
					elif(isinstance(v[i],int)):
						a=a+ '<li>'+str(v[i])+'</li>'
					elif(isinstance(v[i],list)==False):
						self.htmlConvertor(v[i])
				print '</ul></td>'
				print '</tr>'
			elif(isinstance(v,unicode)):
				print '<td>'+ str(v) +'</td>'
				print '</tr>'
			elif(isinstance(v,int)):
				print '<td>'+ str(v) +'</td>'
				print '</tr>'
			else:
				print '<td>'
				self.htmlConvertor(v)
				print '</td></tr>'
		print '</table>'

	def iterJson(self,ordered_json):
		global a
		a=a+ "<table border=\"1\">" 
		for k,v in ordered_json.iteritems():
			a=a+ '<tr>'
			a=a+ '<th>'+ str(k) +'</th>'
			if(isinstance(v,list)):
				a=a+ '<td><ul>'
				for i in range(0,len(v)):
					if(isinstance(v[i],unicode)):
						a=a+ '<li>'+str(v[i])+'</li>'
					elif(isinstance(v[i],int) or isinstance(v,float)):
						a=a+ '<li>'+str(v[i])+'</li>'
					elif(isinstance(v[i],list)==False):
						self.iterJson(v[i])
				a=a+ '</ul></td>'
				a=a+ '</tr>'
			elif(isinstance(v,unicode)):
				a=a+ '<td>'+ str(v) +'</td>'
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
		try:
			for k,v in ordered_json.iteritems():
				pass
			self.iterJson(ordered_json)
		
		except:
			for i in range(0,len(ordered_json)):
				if(isinstance(ordered_json[i],unicode)):
					a=a+ '<li>'+str(ordered_json[i])+'</li>'
				elif(isinstance(ordered_json[i],int) or isinstance(ordered_json[i],float)):
					a=a+ '<li>'+str(ordered_json[i])+'</li>'
				elif(isinstance(ordered_json[i],list)==False):
					self.htmlConvertor(ordered_json[i])	

		return a

	def htmlConvertormain(self,ordered_json):
		global a
		a+='<table border="1">\n'
		for k,v in ordered_json.iteritems():
			a+= '<tr>\n'
			a+= '<th>'+ str(k) +'</th>\n'
			if(isinstance(v,list)):
				a+= '<td><ul>\n'
				for i in range(0,len(v)):
					if(isinstance(v[i],unicode)):
						a+= '<li>'+str(v[i])+'</li>\n'
					elif(isinstance(v[i],int)):
						a+= '<li>'+str(v[i])+'</li>\n'
					elif(isinstance(v[i],list)==False):
						self.htmlConvertor(v[i])
				a+= '</ul></td>\n'
				a+= '</tr>\n'
			elif(isinstance(v,unicode)):
				a+= '<td>'+ str(v) +'</td>\n'
				a+= '</tr>\n'
			elif(isinstance(v,int)):
				a+= '<td>'+ str(v) +'</td>\n'
				a+= '</tr>\n'
			else:
				a+= '<td>\n'
				self.htmlConvertor(v)
				a+= '</td></tr>\n'
		a+= '</table>'
		return a

json2html = JSON()