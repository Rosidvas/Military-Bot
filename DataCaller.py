import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Military_Equipment"] ## Add Databank name here

def send_error(parameter):
    return (f"The {parameter} cannot be found within our catalog.")

# Aircraft ----------------
def getAllPlanes():
    collection = db["aircraft"]
    result = collection.find({}, {"_id": 0, "name": 1, "_class": 1})
    aircraft_list = [{document["name"], document["_class"]} for document in result]
    print(aircraft_list)

    return aircraft_list


def callDataPlane(parameter):
    collection = db["aircraft"]
    result = collection.find_one({"name": parameter})
    
    if result == None:
        result = send_error(parameter)
        
    print(result)
    return result

# Vehicles ----------------
def getAllVehicles():
    collection = db["vehicles"]
    result = collection.find({}, {"_id": 0, "name": 1, "_class": 1})
    vehicle_list = [{document["name"], document["_class"]} for document in result]
    print(vehicle_list)

    return vehicle_list

def callDataVehicle(parameter):
    collection = db["vehicles"]
    result = collection.find_one({"name": parameter})

    if result == None:
        result = send_error(parameter)

    print(result)   
    return result

# Vessels -----------------
def callDataShip(parameter):
    collection = db[""]
    result = collection.find({"name": parameter.Lower})
    return result



