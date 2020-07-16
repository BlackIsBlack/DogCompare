import pymongo

client = pymongo.MongoClient("mongodb+srv://BlackIsBlock:gFu2zQaM5gdA3oxz@objectcompare.2twc4.mongodb.net/ComparisonObjects?retryWrites=true&w=majority")
db = client.ComparisonObjects
objectInfo = db.objectInfo


