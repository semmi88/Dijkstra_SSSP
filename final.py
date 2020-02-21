import inputMetros, inputTrips
import dijkstra

path_metros = 'metro_lines.json'
g,maxEdge = inputMetros.readMetrolines(path_metros)
maxDistance = maxEdge * 100


path_trips = 'trip_records.jsonl'
trips = inputTrips.readTripRecords(path_trips)

distancesCalculatedFrom = set()
shortestPathsFrom = {}
timesVisited = {}

for trip in trips:
    src = trip[0]
    dest = trip[1]
    visitedStations = []
    if ((src not in distancesCalculatedFrom) and (dest not in distancesCalculatedFrom)):
        distances, paths = dijkstra.dijkstra(g, src, maxDistance)
        distancesCalculatedFrom.add(src)
        shortestPathsFrom[src] = paths
        visitedStations = paths[dest]
    elif (src in distancesCalculatedFrom):
        visitedStations = shortestPathsFrom[src][dest]
    elif (dest in distancesCalculatedFrom):
        visitedStations = shortestPathsFrom[dest][src]
    
    #print(visitedStations)

    for s in visitedStations:
        if timesVisited.has_key(s):
            timesVisited[s] = timesVisited[s]+1
        else:
            timesVisited[s] = 1

stationsSorted = list(timesVisited.items())
stationsSorted.sort(key=lambda tup: tup[1])
for s in reversed(stationsSorted):
    print(s)