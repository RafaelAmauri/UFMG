from include.graph import Graph
from include.vertex import Vertex

import heapq

def djikstra(graph: Graph, srcId: int, destId: int) -> list:
    """
        Djikstra's algorithm to find the shortest path between two vertices in a graph

        Inputs:
            graph:  The graph object
            srcId:  The ID of the source vertex
            destId: The ID of the destination vertex

        Outputs:
            shortestPath: a list with the IDs of the vertices that, when traversed, form the shortest path; Starts at srcId and ends at destId
    """

    ## For each vertex, stores its distance to the source vertex. Starts every value at infinite, except for the source vertex
    distanceFromSrc = { vertexId : float('inf') for vertexId in graph.vertices.keys() }
    distanceFromSrc[srcId] = 0
    
    ## For each vertex, stores what other vertex in the graph that led to this one with the shortest path. Think of it as a 'parent' in a tree structure
    originOfVertex  = { vertexId: -1 for vertexId in graph.vertices.keys() }
    visitedVertices = set()

    priorityQueue   = [(0, srcId)]
    while priorityQueue:

        currentVertexDistanceToSrc, currentVertexId = heapq.heappop(priorityQueue)
        # Because we can't update the distances for the elements that are already in the PriorityQueue, we must "reinsert" the updated entry into the PQ.
        # This takes O(lgN) time and is still better than O(N) search for the vertex with the highest priority, so... Yeah.
        if currentVertexId in visitedVertices:
            continue
        
        visitedVertices.add(currentVertexId)

        # Because every vertex has its own "shortest distance from the source" stored in distanceFromSrc, and most start at float('inf'),
        # we need to update them to find the REAL distance that each vertex has to the source.

        # This is done by, for each vertex, putting together the "original" value in distanceFromSrc for currentVertex and the weight of the edge
        # that connects the currentVertex to the neighbor. If this result is lower than the one stored in distanceFromSrc for the neighbor, then we found
        # a shorter path going from src to the neighbor.

        # This wouldn't work if all the vertices had float('inf') in distanceFromSrc, but here's why the src node has distance 0:
        # because 0 + any weight < float('inf'), and all neighbors to the currentVertex start at distance float('inf'). This way, we update the
        # distances one by one.

        # Lastly, we add the neighbor to the stack so that it becomes the next iteration's currentVertex.
        for neighborId, neighborWeight in graph.vertices[currentVertexId].neighbors.items():
            distanceToNeighbor = currentVertexDistanceToSrc + neighborWeight

            if distanceToNeighbor < distanceFromSrc[neighborId]:
                distanceFromSrc[neighborId] = distanceToNeighbor
                heapq.heappush(priorityQueue, (distanceToNeighbor, neighborId))
                originOfVertex[neighborId]  = currentVertexId

    # Now that we know each vertex's shortest distance to the src, it is trivial to find the shortest path from src to dest. 
    # Starting at dest, check the currentVertex's origin vertex (the one that we have stored in originOfVertex) and then update
    # currentVertex to be the origin point for the original currentVertex. We do so until the origin point of a vertex is -1, and that's either when
    # currentVertex is the source vertex, or when no valid path could be found for a given vertex. 
    
    shortestPath    = []
    currentVertexId = destId
    while originOfVertex[currentVertexId] != -1:
        shortestPath.append(currentVertexId)
        currentVertexId = originOfVertex[currentVertexId]

    shortestPath.reverse()
    shortestPath.insert(0, srcId)
    
    return shortestPath



if __name__ == '__main__':
    vertices = [Vertex(i) for i in range(0, 13)]

    g = Graph(vertices[0])
    [g.addVertex(v) for v in vertices]

    # This graph can be visualized in https://www.youtube.com/watch?v=GazC3A4OQTE&t=79
    g.addEdge(vertices[0], vertices[ord('A') - 64], 7)
    g.addEdge(vertices[0], vertices[ord('B') - 64], 2)
    g.addEdge(vertices[0], vertices[ord('C') - 64], 3)
    g.addEdge(vertices[ord('A') - 64], vertices[ord('B') - 64], 3)
    g.addEdge(vertices[ord('A') - 64], vertices[ord('D') - 64], 4)
    g.addEdge(vertices[ord('B') - 64], vertices[ord('D') - 64], 4)
    g.addEdge(vertices[ord('B') - 64], vertices[ord('H') - 64], 1)
    g.addEdge(vertices[ord('C') - 64], vertices[ord('L') - 64], 2)
    g.addEdge(vertices[ord('D') - 64], vertices[ord('F') - 64], 5)
    g.addEdge(vertices[ord('E') - 64], vertices[ord('G') - 64], 2)
    g.addEdge(vertices[ord('E') - 64], vertices[ord('K') - 64], 5)
    g.addEdge(vertices[ord('F') - 64], vertices[ord('H') - 64], 3)
    g.addEdge(vertices[ord('G') - 64], vertices[ord('H') - 64], 2)
    g.addEdge(vertices[ord('I') - 64], vertices[ord('L') - 64], 4)
    g.addEdge(vertices[ord('I') - 64], vertices[ord('J') - 64], 6)
    g.addEdge(vertices[ord('I') - 64], vertices[ord('K') - 64], 4)
    g.addEdge(vertices[ord('J') - 64], vertices[ord('L') - 64], 4)
    g.addEdge(vertices[ord('J') - 64], vertices[ord('K') - 64], 4)

    print(djikstra(g, 0, ord('E') - 64))