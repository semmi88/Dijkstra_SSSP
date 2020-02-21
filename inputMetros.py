import json

def readMetrolines(path):
    g = {}
    maxEdge = 0
    with open(path) as file:
        data = file.read()
        for line in json.loads(data):
            stations = line['stations']
            for i in range(len(stations)-1):
                distance = abs(stations[i]['time'] - stations[i+1]['time'])
                if (distance>maxEdge):
                    maxEdge=distance
                a = stations[i]['name']
                b = stations[i+1]['name']
                if (g.has_key(a)):
                    g[a].append((b,distance))
                else:
                    g[a] = [(b,distance)]

                if (g.has_key(b)):
                    g[b].append((a,distance))
                else:
                    g[b] = [(a,distance)]
    return g, maxEdge



def printResult(g,maxEdge):
    print(maxEdge)
    print(len(g.keys()))
    for entry in g.items():
        print('')
        print(entry[0])
        print('')
        for n in entry[1]:
            print(n)

def test():
    path = 'metro_lines.json'
    g,maxEdge = readMetrolines(path)
    printResult(g, maxEdge)

#test()