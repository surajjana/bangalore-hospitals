from requests.utils import quote
from subprocess import call
import json

fl = open("hospitals_pincode.json","a")

fd = open("data_final.json","r")
data = fd.read()

json_data = json.loads(data)

for i in range(0,1):
	print i

	addr = json_data["hospitals"][i]["address"]

	e_addr = quote(addr)

	api = 'http://www.getpincode.info/api/pincode?q='+e_addr

	call('curl "'+api+'" > pincode.json',shell=True)

	fo = open("pincode.json","r")
	data_p = fo.read()

	json_data_p = json.loads(data_p)

	pincode = json_data_p["pincode"]
	name = json_data["hospitals"][i]["name"]

	fl.write('{"id":'+str(i+1)+',"name":"'+name+'","address":"'+addr+'","pincode":"'+str(pincode)+'"},')
