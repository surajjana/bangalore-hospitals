from subprocess import call
import json

api = 'http://maps.google.com/maps/api/geocode/json?address='
addr = '15Th Cross 3Rd Blk Jayanagar,Banaglore, Bangalore, Karnataka'

addr = addr.replace(" ", "+")

api_url = api+addr+'&sensor=false'

call('curl "'+api_url+'" > test_2.json',shell=True)

fo = open("test_2.json","r")
data = fo.read()

json_data = json.loads(data)

print json_data["results"][0]["geometry"]["location"]["lat"]
print json_data["results"][0]["geometry"]["location"]["lng"]
print json_data["status"]