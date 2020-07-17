import pymongo
apiKey = open('/home/pi/apikey.txt','r').read()
print(apiKey)
client = pymongo.MongoClient(apiKey)
db = client.ComparisonObjects
objectInfo = db.objectInfo
firstDog = ""
secondDog = ""
def newDog():
    global firstDog
    global secondDog
    try:
        db.comparisons.remove({})
        
    except:
        try:
            objectInfo.aggregate([{ "$sample": { "size": 2 } },{ "$out" : "comparisons"}])
        except:
            pass
    comparisonDogs = []
    for i in db.comparisons.find():
        comparisonDogs.append(i)

    firstDog = objectInfo.find({ "Name": comparisonDogs[0]["Name"] })
    secondDog = objectInfo.find({ "Name": comparisonDogs[1]["Name"] })

def SetElo(Dog1ID, Dog2ID, winner):
    Dog1 = objectInfo.find({ "Name": Dog1ID })
    Dog2 = objectInfo.find({ "Name": Dog2ID })

    Dog1ELOHold = int(Dog1[0]["ELO"])
    Dog2ELOHold = int(Dog2[0]["ELO"])

    Dog1Wins = int(Dog1[0]["Wins"])
    Dog2Wins = int(Dog2[0]["Wins"])
    Dog1Losses = int(Dog1[0]["Losses"])
    Dog2Losses = int(Dog2[0]["Losses"])
    if (winner == str(1)):
        Dog1Wins +=1
        Dog2Losses +=1
    else:
        Dog2Wins += 1
        Dog1Losses +=1
    Dog1ELO = Dog2ELOHold + 400 * (Dog1Wins - Dog1Losses)
    Dog2ELO = Dog1ELOHold + 400 * (Dog2Wins - Dog2Losses)
    print(Dog1ELO)
    print(Dog2ELO)
    try:
        objectInfo.update_one({ "_id": Dog1[0]["_id"] }, { "$set": { "ELO": str(Dog1ELO), "Wins": str(Dog1Wins), "Losses": str(Dog1Losses) }})
    except:
        pass
    try:
        objectInfo.update_one({ "_id": Dog2[0]["_id"] }, { "$set": { "ELO": str(Dog2ELO), "Wins": str(Dog2Wins), "Losses": str(Dog2Losses) }})
    except:
        pass
