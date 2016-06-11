import json
import os

class RDPList:

	configFilename="rdplist.json"

	def test_json(self):
		for list in self.config['lists']:
			print(list['listname'])

	def create_json(self):
		tempConfig={"config":{
			"fullscreen":"no",
			"width":"1800",
    	"height":"950",
    	"console":"yes",
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
		if(freerdp):
			if(fullscreen):
				my_command='xfreerdp'+" /u:"+target['user']+" /d:"+target['domain']+" /p:"+target['password']+" /admin /cert-ignore /drive:home,/home/bobman /f /v:"+target['ip']+' &'
			else:
				my_command='xfreerdp'+" /u:"+target['user']+" /d:"+target['domain']+" /p:"+target['password']+" /admin /cert-ignore /drive:home,/home/bobman /w:1800 /h:950 /v:"+target['ip']+' &'
		else:
			if(fullscreen):
				my_command='rdesktop'+" -u"+target['user']+" -d"+target['domain']+" -p"+target['password']+" -0 -r disk:home=/home/bobman/ -f "+target['ip']+'>/dev/null 2>&1 &'
			else:
				my_command='rdesktop'+" -u"+target['user']+" -d"+target['domain']+" -p"+target['password']+" -0 -r disk:home=/home/bobman/ -g1800x950 "+target['ip']+'>/dev/null 2>&1 &'
		print(my_command)
		os.system(my_command)

if __name__ == '__main__':
	rdp = RDPList()
	rdp.load_json()
	rdp.test_json()
