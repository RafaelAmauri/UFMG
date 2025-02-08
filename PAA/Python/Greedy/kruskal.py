from include.graph import Graph
from include.vertex import Vertex

import heapq


def kruskal(graph: Graph):
    '''
        Kruskal's algorithm to find a Minimum Spanning Tree, 
        which is a version of the input graph where all the vertices in 
        the original graph are also included and the weight of the edges in the MST must
        be the lowest one possible. The MST must also be acyclic.

        Inputs:
            graph: A Graph object
            initialVertexId: the ID of the first vertex of the MST.
        Outputs:
            mst: A graph object. It contains the MST.
    '''

    mst = Graph(graph.root)
    priorityQueue = []

    # Add a copy of all vertices in the graph to the MST
    [mst.addVertex(v.copy()) for v in graph.vertices.values()]
    
    # Add all edges in the graph to the priority queue
    for vertexId, vertex in graph.vertices.items():
        for neighborId, neighborWeight in vertex.neighbors.items():
            heapq.heappush(priorityQueue, (neighborWeight, vertexId, neighborId))

    # While we have less than V-1 edges in the graph, add the lowest-weight edge as long as
    # it does not form a cycle.
    while mst.numEdges < len(mst.vertices)-1:
        weight, srcId, destId = heapq.heappop(priorityQueue)
        
        mst.addEdge(mst.vertices[srcId], mst.vertices[destId], weight)
        
        # This right here makes this the worst Kruskal in the world. While it works, we
        # should be using Union-Find for a more efficient algorithm.
        # https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
        if dfsHasCycle(mst, srcId):
            mst.removeEdge(mst.vertices[srcId], mst.vertices[destId])

    return mst


def dfsHasCycle(graph: Graph, startVertex) -> bool:
    """
        Uses DFS to check if a cycle exists in graph

        Input:
            graph: a graph element
        
        Output:
            hasCycle: a boolean indicating whether a cycle exists
    """

    hasCycle        = False
    stack           = [(startVertex, -1)]
    visitedVertices = set()
    parentId        = -1
    while stack and not hasCycle:
        currentVertexId, parentId = stack.pop(0)
        currentVertex             = graph.vertices[currentVertexId]
        visitedVertices.add(currentVertexId)

        for neighborId in currentVertex.neighbors.keys():
            if neighborId in visitedVertices and neighborId != parentId:
                hasCycle = True
                break
            
            if neighborId not in visitedVertices:
                stack.append((neighborId, currentVertexId))
    
    return hasCycle


if __name__ == '__main__':
    vertices = [Vertex(i) for i in range(0, 9)]

    g = Graph(vertices[0])
    [g.addVertex(v) for v in vertices]

    # This graph can be visualized in https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
    g.addEdge(vertices[0], vertices[1], 4)
    g.addEdge(vertices[0], vertices[7], 8)
    g.addEdge(vertices[1], vertices[2], 8)
    g.addEdge(vertices[1], vertices[7], 11)
    g.addEdge(vertices[2], vertices[3], 7)
    g.addEdge(vertices[2], vertices[8], 2)
    g.addEdge(vertices[2], vertices[5], 4)
    g.addEdge(vertices[3], vertices[4], 9)
    g.addEdge(vertices[3], vertices[5], 14)
    g.addEdge(vertices[4], vertices[5], 10)
    g.addEdge(vertices[5], vertices[6], 2)
    g.addEdge(vertices[6], vertices[8], 6)
    g.addEdge(vertices[6], vertices[7], 1)
    g.addEdge(vertices[7], vertices[8], 7)

    mst = kruskal(g)
    print(mst)