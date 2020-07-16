import pymongo

client = pymongo.MongoClient("mongodb+srv://***REMOVED***@objectcompare.2twc4.mongodb.net/ComparisonObjects?retryWrites=true&w=majority")
db = client.ComparisonObjects
objectInfo = db.objectInfo


