import re

fo = open("test2.html","r")
data = fo.read()
rxp = re.findall(r'<div class="hospital">(.*?)</div>',data,re.DOTALL)
rxp1 = re.findall(r'<li>(.*?)</li>',rxp[0],re.DOTALL)

email = rxp1[1].split(": ")
website = rxp1[2].split(": ")
contact = rxp1[3].split(": ")
mobile = rxp1[4].split(": ")
fax = rxp1[5].split(": ")

addr = re.findall(r'<u>(.*?)</u>',rxp1[0],re.DOTALL)
addr = addr[0].split("\t")

print addr[8]