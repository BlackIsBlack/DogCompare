import pymongo
apiKey = open('/home/pi/apikey.txt','r').read()
client = pymongo.MongoClient(apiKey)
db = client.ComparisonObjects
objectInfo = db.objectInfo
print(db.list_collection_names())


