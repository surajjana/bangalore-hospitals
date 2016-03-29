import re
import json
from subprocess import call

fl = open("data.json","a")

fd = open("data_list.json","r")
json_data = fd.read()
json_data = json.loads(json_data)

for l in range(0,1348):

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
	
	if len(departments) == 0:
		dept_data = '[]'
		str_data = '{"id":'+str(l+1)+',"name":"'+json_data["hospital_names"][l]["name"]+'","departments":'+dept_data+',"category":"'+category[0]+'","type":"'+h_type[0]+'","facilities":[{"Ambulance":"'+ambulance[1]+'","Lab Attached":"'+lab_attached[1]+'","Pharmacy Attached":"'+pharmacy[1]+'","Canteen":"'+canteen[1]+'","Cashless Mediclaim":"'+mediclaim[1]+'","Organ Transplants":"'+transplant[1]+'"}]},'
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

		str_data = '{"id":'+str(l+1)+',"name":"'+json_data["hospital_names"][l]["name"]+'","departments":'+dept_data+',"category":"'+category[0]+'","type":"'+h_type[0]+'","facilities":[{"Ambulance":"'+ambulance[1]+'","Lab Attached":"'+lab_attached[1]+'","Pharmacy Attached":"'+pharmacy[1]+'","Canteen":"'+canteen[1]+'","Cashless Mediclaim":"'+mediclaim[1]+'","Organ Transplants":"'+transplant[1]+'"}]},'
		# print str_data
		fl.write(str_data)