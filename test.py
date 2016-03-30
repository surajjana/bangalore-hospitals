import json

count = 0

fo = open("data_final.json","r")
data = fo.read()

json_data = json.loads(data)

for i in range(0,1347):
	lat = json_data["hospitals"][i]["location"][0]["lat"]

	#print i+1,". ",str(lat)

	if str(lat) == '0.0':
		count = count + 1

print "Count : ",count