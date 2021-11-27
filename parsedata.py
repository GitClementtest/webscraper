import json

with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

#Get the dates of each tweet
for i in jsonData:
	print i['date']

#for i in jsonData:
#    if "obama" in i['tweet'].lower():
#        print i
