import json

def readTripRecords(path):
    trips = []
    with open(path) as file:
        data = file.readlines()
        for n in data:
            trip = json.loads(n)
            trips.append((trip['origin'], trip['destination']))
    return trips

def test():
    path = 'trip_records.jsonl'
    trips = readTripRecords(path)
    for trip in trips:
        print(trip[0] + " - " + trip[1])

#test()