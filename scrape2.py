import re
import json
from subprocess import call
import time

fl = open("data_final.json","a")

fd = open("data_list.json","r")
json_data = fd.read()
json_data = json.loads(json_data)

for l in range(1343,1347):

	print l

	call("curl '"+json_data["hospital_names"][l]["url"]+"' > test_new.html",shell=True)

	fo = open("test_new.html", "r")
	data = fo.read()

	general = re.findall(r'<ul id="list-general">(.*?)</ul>',data,re.DOTALL)
	category = re.findall(r'<li><label>Hospital / Clinic</label>: (.*?)</li>',general[0],re.DOTALL)
	h_type = re.findall(r'<li><label>Hospital Type</label>: (.*?)</li>',general[0],re.DOTALL)

	# opd_timing = re.findall(r'<ul id="list-timings">(.*?)</ul>',data,re.DOTALL)
	# opd_timing = re.findall(r'<li><i class="fa fa-clock-o faj"></i><label>OPD</label>: (.*?)</li>',opd_timing[0],re.DOTALL)

	# description = re.findall(r'<div class="description">(.*?)</div>',data,re.DOTALL)

	facilities = re.findall(r'<ul id="list-facilities">(.*?)</ul>',data,re.DOTALL)
	facilities = re.findall(r'<li>(.*?)</li>',facilities[0],re.DOTALL)


	ambulance = facilities[0].split(": ")
	lab_attached = facilities[1].split(": ")
	pharmacy = facilities[2].split(": ")
	canteen = facilities[3].split(": ")
	mediclaim = facilities[4].split(": ")
	transplant = facilities[5].split(": ")

	departments = re.findall(r'<ul id="list-specialization">(.*?)</ul>',data,re.DOTALL)

	rxp = re.findall(r'<div class="hospital">(.*?)</div>',data,re.DOTALL)
	rxp1 = re.findall(r'<li>(.*?)</li>',rxp[0],re.DOTALL)

	email = rxp1[1].split(": ")
	website = rxp1[2].split(": ")
	contact = rxp1[3].split(": ")
	mobile = rxp1[4].split(": ")

	addr = re.findall(r'<u>(.*?)</u>',rxp1[0],re.DOTALL)
	addr = addr[0].split("\t")

	api = 'http://maps.google.com/maps/api/geocode/json?address='

	addr_l = addr[8]
	addr_l = addr_l.replace(" ", "+")

	api_url = api+addr_l+'&sensor=false'

	# time.sleep(1)

	call('curl "'+api_url+'" > test_1.json',shell=True)

	fo = open("test_1.json","r")
	data_l = fo.read()

	json_data_l = json.loads(data_l)

	if json_data_l["status"] == "OK":
		lat = json_data_l["results"][0]["geometry"]["location"]["lat"]
		lng = json_data_l["results"][0]["geometry"]["location"]["lng"]
	else:
		lat = 0.00
		lng = 0.00
	
	if len(departments) == 0:
		dept_data = '[]'
		if len(rxp1) == 5:
			str_data = '{"id":'+str(l+1)+',"name":"'+json_data["hospital_names"][l]["name"]+'","departments":'+dept_data+',"category":"'+category[0]+'","type":"'+h_type[0]+'","facilities":[{"Ambulance":"'+ambulance[1]+'","Lab Attached":"'+lab_attached[1]+'","Pharmacy Attached":"'+pharmacy[1]+'","Canteen":"'+canteen[1]+'","Cashless Mediclaim":"'+mediclaim[1]+'","Organ Transplants":"'+transplant[1]+'"}],"address":"'+addr[8]+'","email":"'+email[1]+'","website":"'+website[1]+'","contact":"'+contact[1]+'","mobile":"'+mobile[1]+'","fax":"","location":[{"lat":'+str(lat)+',"lng":'+str(lng)+'}]},'
		else:
			fax = rxp1[5].split(": ")
			str_data = '{"id":'+str(l+1)+',"name":"'+json_data["hospital_names"][l]["name"]+'","departments":'+dept_data+',"category":"'+category[0]+'","type":"'+h_type[0]+'","facilities":[{"Ambulance":"'+ambulance[1]+'","Lab Attached":"'+lab_attached[1]+'","Pharmacy Attached":"'+pharmacy[1]+'","Canteen":"'+canteen[1]+'","Cashless Mediclaim":"'+mediclaim[1]+'","Organ Transplants":"'+transplant[1]+'"}],"address":"'+addr[8]+'","email":"'+email[1]+'","website":"'+website[1]+'","contact":"'+contact[1]+'","mobile":"'+mobile[1]+'","fax":"'+fax[1]+'","location":[{"lat":'+str(lat)+',"lng":'+str(lng)+'}]},'
		# print str_data
		fl.write(str_data)
	else:
		departments = re.findall(r'<li><i class="fa fa-folder faj"></i>(.*?)</li>',departments[0],re.DOTALL)

		dept_data = '['

		for m in range(0,len(departments)):
			if m == len(departments) - 1:
				dept_data += '{"d_name":"'+departments[m]+'"}]'
			else:
				dept_data += '{"d_name":"'+departments[m]+'"},'

		if len(rxp1) == 5:
			str_data = '{"id":'+str(l+1)+',"name":"'+json_data["hospital_names"][l]["name"]+'","departments":'+dept_data+',"category":"'+category[0]+'","type":"'+h_type[0]+'","facilities":[{"Ambulance":"'+ambulance[1]+'","Lab Attached":"'+lab_attached[1]+'","Pharmacy Attached":"'+pharmacy[1]+'","Canteen":"'+canteen[1]+'","Cashless Mediclaim":"'+mediclaim[1]+'","Organ Transplants":"'+transplant[1]+'"}],"address":"'+addr[8]+'","email":"'+email[1]+'","website":"'+website[1]+'","contact":"'+contact[1]+'","mobile":"'+mobile[1]+'","fax":"","location":[{"lat":'+str(lat)+',"lng":'+str(lng)+'}]},'
		else:
			fax = rxp1[5].split(": ")
			str_data = '{"id":'+str(l+1)+',"name":"'+json_data["hospital_names"][l]["name"]+'","departments":'+dept_data+',"category":"'+category[0]+'","type":"'+h_type[0]+'","facilities":[{"Ambulance":"'+ambulance[1]+'","Lab Attached":"'+lab_attached[1]+'","Pharmacy Attached":"'+pharmacy[1]+'","Canteen":"'+canteen[1]+'","Cashless Mediclaim":"'+mediclaim[1]+'","Organ Transplants":"'+transplant[1]+'"}],"address":"'+addr[8]+'","email":"'+email[1]+'","website":"'+website[1]+'","contact":"'+contact[1]+'","mobile":"'+mobile[1]+'","fax":"'+fax[1]+'","location":[{"lat":'+str(lat)+',"lng":'+str(lng)+'}]},'
		# print str_data
		fl.write(str_data)