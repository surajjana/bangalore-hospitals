import re
import json
from subprocess import call

fd = open("data_list.json","a")

for i in range(89,91):

	print i

	call("curl 'https://www.hospitalkhoj.com/hospitals/bangalore/page-"+str(i)+"' > test2.html", shell=True)

	fo = open("test2.html", "r")
	data = fo.read()
	for j in range(1,16):
		rxp1 = re.findall(r'<ul id="college-list">(.*?)</ul>',data,re.DOTALL)
		res_val = rxp1[0].split('<li  >')
		rxp2 = re.findall(r'<div class="cl-list-name">(.*?)</div>',res_val[j],re.DOTALL)
		rxp3 = re.findall(r''+str(">\n")+'(.*?)</a>',rxp2[0],re.DOTALL)
		res_val = rxp3[0].split("\t")

		rxp4 = re.findall(r'href='+str("\'")+'(.*?)'+"\'",rxp2[0],re.DOTALL)

		# print "Name : ",res_val[6]
		# print "URL : https://www.hospitalkhoj.com"+rxp4[0]

		fd.write('{"name":"'+res_val[6]+'","url":"https://www.hospitalkhoj.com'+rxp4[0]+'"},')
fd.close()