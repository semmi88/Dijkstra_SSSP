def dijkstra(graph, source, maxDistance):
    distances, unvisited, paths = prepareForShortestPathCalculation(graph, maxDistance)
    unvisited.remove(source)
    distances[source] = 0
    updateDistancesAndPathsThroughNode(source, distances, paths, graph[source])
    while len(unvisited)>0:
        closestNode = getClosestUnvisitedNode(distances, unvisited)
        updateDistancesAndPathsThroughNode(closestNode, distances, paths, graph[closestNode])
        unvisited.remove(closestNode)
    updatePathsWithDestination(paths)
    return distances, paths

def getClosestUnvisitedNode(distances, unvisited):
    unInitialized = True
    minDistance = 0
    closestNode = ''
    for node in unvisited:
        if (unInitialized):
            minDistance = distances[node]
            closestNode = node
            unInitialized = False
        elif (distances[node] < minDistance):
            minDistance = distances[node]
            closestNode = node
    return closestNode

def updateDistancesAndPathsThroughNode(throughNodeName, distances, paths, neighborList):
    throughNodeDistance = distances[throughNodeName]
    for n in neighborList:
        neighborNodeName = n[0]
        neighborNodeDistance = n[1]
        
        currentDistance = distances[neighborNodeName]
        alternateDistance = throughNodeDistance+neighborNodeDistance
        
        currentPath = paths[neighborNodeName]
        alternatePath = list(paths[throughNodeName])
        alternatePath.append(throughNodeName)
        
        if (alternateDistance<currentDistance):
            distances[neighborNodeName]=alternateDistance
            paths[neighborNodeName]=alternatePath
        elif (alternateDistance==currentDistance):
            if alphabeticSuperiority(alternatePath,currentPath):
                distances[neighborNodeName]=alternateDistance
                paths[neighborNodeName]=alternatePath

def alphabeticSuperiority(pathOne, pathTwo):
    minLenght = min(len(pathOne),len(pathTwo))
    for i in range(minLenght):
        if pathOne[i] > pathTwo[i]:
            return False
    return True

def prepareForShortestPathCalculation(graph, maxDistance):
    unvisited = set()
    paths = {}
    distances = {}
    for entry in graph.items():
        node = entry[0]
        neighborList = entry[1]
        distances[node] = maxDistance
        unvisited.add(node)
        paths[node] = []
    return distances, unvisited, paths

#max = 1000
#distances = {'A':max,'B':max,'C':max,'D':max,'E':max}
#unvisited = set(['A','B','C','D','E'])
#paths = {'A':[],'B':[],'C':[],'D':[],'E':[]}

def updatePathsWithDestination(paths):
    for entry in paths.items():
        destination = entry[0]
        entry[1].append(destination)

def test():
    g = {}
    g['A'] = [('B',2),('C',1)]
    g['B'] = [('A',2),('D',2)]
    g['C'] = [('A',1),('D',2)]
    g['D'] = [('E',1), ('C',2),('B',2)]
    g['E'] = [('D',1)]


    distances, paths = dijkstra(g, 'A', 1000)
    for pairs in distances.items():
        print(pairs)

    for pairs in paths.items():
        print(pairs)

#test()