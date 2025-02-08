# Solução Beecrowd 1447 https://judge.beecrowd.com/en/problems/view/1447

import math
import heapq

def djikstra(adjacencyList: list, srcId: int, destId: int) -> list:
    distanceFromSrc = { vertexId : float('inf') for vertexId in adjacencyList.keys() }
    distanceFromSrc[srcId] = 0
    
    originOfVertex  = { vertexId: -1 for vertexId in adjacencyList.keys() }
    visitedVertices = set()

    priorityQueue          = [(0, srcId)]
    while priorityQueue:
        currentVertexDistanceToSrc, currentVertexId = heapq.heappop(priorityQueue)
        if currentVertexId in visitedVertices:
            continue
        
        visitedVertices.add(currentVertexId)

        for neighborId, (neighborWeight, isUsed) in adjacencyList[currentVertexId].items():
            if isUsed:
                continue

            distanceToNeighbor = currentVertexDistanceToSrc + neighborWeight

            if distanceToNeighbor < distanceFromSrc[neighborId]:
                distanceFromSrc[neighborId] = distanceToNeighbor
                heapq.heappush(priorityQueue, (distanceToNeighbor, neighborId))
                originOfVertex[neighborId]  = currentVertexId


    shortestPath    = []
    currentVertexId = destId
    while originOfVertex[currentVertexId] != -1:
        shortestPath.append(currentVertexId)
        price = adjacencyList[originOfVertex[currentVertexId]][currentVertexId][0]
        adjacencyList[originOfVertex[currentVertexId]][currentVertexId] = (price, True)

        currentVertexId = originOfVertex[currentVertexId]

    shortestPath.reverse()
    shortestPath.insert(0, srcId)
    
    return shortestPath


try:
    instance  = 1
    while(True):
        nCities, nRoutes = map(int, input().split(" ")[ : 2])

        adjacencyList = { i : {} for i in range(nCities) }
        allPaths      = []
        paidAmount    = 0
        foundPath     = False
        
        for i in range(nRoutes):
            city1, city2, price = map(int, input().split(" ")[ : 3])

            city1 -= 1
            city2 -= 1

            adjacencyList[city1][city2] = (price, False)
            adjacencyList[city2][city1] = (price, False)

        nFriends, nFreeSeats = map(int, input().split(" ")[ : 2])

        if nRoutes > 0:
            for i in range(math.ceil(nFriends/nFreeSeats)):
                shortestPath = djikstra(adjacencyList, 0, nCities-1)

                foundPath = True if len(shortestPath) > 1 else False
                allPaths.append(shortestPath)

            if foundPath:
                for path in allPaths:
                    for i in range(len(path)-1):
                        currentCity = path[i]
                        nextCity    = path[i+1]

                        if(adjacencyList[currentCity][nextCity][1] != adjacencyList[nextCity][currentCity][1]):
                            currentPrice = adjacencyList[currentCity][nextCity][0]
                            paidAmount  += currentPrice * min(nFreeSeats, nFriends)

                            adjacencyList[currentCity][nextCity] = (currentCity, False)
                            adjacencyList[nextCity][currentCity] = (currentCity, False)
                    
                    nFriends -= nFreeSeats

        print(f"Instancia {instance}")
        if not foundPath:
            print("impossivel\n")
        else:
            print(paidAmount, end="\n\n")
        allPaths.clear()
        adjacencyList.clear()
        instance += 1
            

except EOFError:
    pass