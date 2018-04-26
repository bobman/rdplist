import json
import os

class RDPList:

	configFilename="rdplist.json"

	def __init__(self):
		self.load_json()

	def test_json(self):
		for list in self.config['lists']:
			print(list['listname'])

	def create_json(self):
		tempConfig={"config":{
			"fullscreen":False,
			"width":"1800",
    	"height":"950",
    	"console":True,
    	"drive":"home,/home"
		},"lists":[
			{
				"listname":"change rdplist.json",
				"targets":[
					{
						"name": "some host",
	          "ip": "127.0.0.1",
	          "domain": "somedomain",
	          "user": "username",
	          "password": "secretpassword"
					}
				]
			}
		]};
		with open(self.configFilename,"w") as data_file:
			json.dump(tempConfig,data_file)

	def get_lists(self):
		return self.config['lists']

	def load_json(self):
		if(not os.path.isfile(self.configFilename)):
			self.create_json()
		with open(self.configFilename) as data_file:
			self.config = json.load(data_file)

	def start_rdp(self,target,fullscreen=False,freerdp=True):
		options = "/u:"+target['user']+" /d:"+target['domain']+" /p:"+target['password']+" /v:"+target['ip']+" /cert-ignore /t:\""+target['name']+"\" /compression /clipboard"
		
		if(self.config['config']['fullscreen']):
			options = options + " /f"
		else:
			options = options + "  /disp /dynamic-resolution /w:"+self.config['config']['width']+" /h:"+self.config['config']['height']

		if(self.config['config']['console']):
			options = options + " /admin"

		if(self.config['config']['drive']!=""):
			options = options + " /drive:"+self.config['config']['drive']
		
		my_command='/opt/freerdp-nightly/bin/xfreerdp '+options+' &'
		
		print(my_command)
		os.system(my_command)

if __name__ == '__main__':
	rdp = RDPList()
	#rdp.load_json()
	rdp.test_json()
