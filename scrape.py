import re
import json
from subprocess import call

json_data = '{"hospital_names":['

for j in range(7,12):
	print j
	call("curl 'https://www.hospitalkhoj.com/hospitals/bangalore/page-"+str(j)+"' > test1.html", shell=True)

	fo = open("test1.html", "r")
	data = fo.read()

	for i in range(1,16):
		#print i
		rxp1 = re.findall(r'<ul id="college-list">(.*?)</ul>',data,re.DOTALL)
		res_val = rxp1[0].split('<li  >')
		rxp2 = re.findall(r'<div class="cl-list-name">(.*?)</div>',res_val[i],re.DOTALL)
		#print rxp2
		rxp3 = re.findall(r''+str(">\n")+'(.*?)</a>',rxp2[0],re.DOTALL)
		#print rxp3
		res_val = rxp3[0].split("\t")

		# print i,". ",res_val[6]
		json_data += '{"name":"'+res_val[6]+'"},'
json_data += ']}'

fd = open("data1.json", "w")
fd.write(json_data)
fd.close()

# json_data = json.loads(json_data)

# for i in range(0,15):
# 	print i+1,". ",json_data["hospital_names"][i]["name"]