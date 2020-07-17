import pymongo
apiKey = open('/home/pi/apikey.txt','r').read()
client = pymongo.MongoClient(apiKey)
db = client.ComparisonObjects
objectInfo = db.objectInfo

try:
    db.comparisons.remove({})
    
except:
    try:
        print(objectInfo.aggregate([{ "$sample": { "size": 2 } },{ "$out" : "comparisons"}]))
    except:
        print("Done")
comparisonDogs = []
for i in db.comparisons.find():
    comparisonDogs.append(i)

firstDog = objectInfo.find({ "Name": comparisonDogs[0]["Name"] })
secondDog = objectInfo.find({ "Name": comparisonDogs[1]["Name"] })
print(f'Dog #1: {comparisonDogs[0]["Name"]}, {comparisonDogs[0]["Image"]}')
print(f'Dog #2: {comparisonDogs[1]["Name"]}, {comparisonDogs[1]["Image"]}')

def SetElo(Dog1ID, Dog2ID, winner):
    Dog1 = objectInfo.find({ "_id": Dog1ID[0]["_id"] })
    Dog2 = objectInfo.find({ "_id": Dog2ID[0]["_id"] })

    Dog1ELOHold = int(Dog1[0]["ELO"])
    Dog2ELOHold = int(Dog2[0]["ELO"])

    Dog1Wins = int(Dog1[0]["Wins"])
    Dog2Wins = int(Dog2[0]["Wins"])
    Dog1Losses = int(Dog1[0]["Losses"])
    Dog2Losses = int(Dog2[0]["Losses"])
    if (winner == 1):
        Dog1Wins +=1
        Dog2Losses +=1
    else:
        Dog2Wins += 1
        Dog1Losses +=1
    Dog1ELO = Dog2ELOHold + 400 * (Dog1Wins - Dog1Losses)
    Dog2ELO = Dog1ELOHold + 400 * (Dog2Wins - Dog2Losses)
    try:
        objectInfo.update_one({ "_id": Dog1ID[0]["_id"] }, { "$set": { "ELO": str(Dog1ELO), "Wins": str(Dog1Wins), "Losses": str(Dog1Losses) }})
    except:
        pass
    try:
        objectInfo.update_one({ "_id": Dog2ID[0]["_id"] }, { "$set": { "ELO": str(Dog2ELO), "Wins": str(Dog2Wins), "Losses": str(Dog2Losses) }})
    except:
        pass
dogWinner = int(input("Which dog is cuter?"))
SetElo(firstDog, secondDog, dogWinner)
    
    