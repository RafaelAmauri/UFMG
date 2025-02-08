from include.graph import Graph
from include.vertex import Vertex

import heapq

def prim(graph: Graph, initialVertexId: int):
    '''
        Prim's algorithm to find a Minimum Spanning Tree, 
        which is a version of the input graph where all the vertices in 
        the original graph are also included and the weight of the edges in the MST must
        be the lowest one possible. The MST must also be acyclic.

        Inputs:
            graph: A Graph object
            initialVertexId: the ID of the first vertex of the MST.
        Outputs:
            mst: A graph object. It contains the MST.
    '''

    mst = Graph(Vertex(initialVertexId))
    priorityQueue       = []
    includedVertices    = set()
    
    # Add initialVertexId to set of vertices that are connected in the MST
    includedVertices.add(initialVertexId)

    # Add a copy of all vertices in the graph to the MST
    [mst.addVertex(v.copy()) for v in graph.vertices.values()]

    # Push all of the initial vertex's edges to priority queue
    for neighborId, neighborWeight in graph.vertices[initialVertexId].neighbors.items():
        heapq.heappush(priorityQueue, (neighborWeight, initialVertexId, neighborId))

    while len(includedVertices) < len(graph.vertices):                
        # Pops the edge with lowest weight
        weight, srcId, destId = heapq.heappop(priorityQueue)
        
        # Skip edges that connect to already included vertices
        if destId in includedVertices:
            continue
        
        # Add edge to the MST
        mst.addEdge(mst.vertices[destId], mst.vertices[srcId], weight)

        includedVertices.add(destId)

        for neighborId, neighborWeight in graph.vertices[destId].neighbors.items():
            heapq.heappush(priorityQueue, (neighborWeight, destId, neighborId))


    return mst


if __name__ == '__main__':
    v0 = Vertex(0)
    g  = Graph(v0)

    [g.addVertex(Vertex(i)) for i in range(1, 9)]

    # This graph can be visualized in https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
    g.addEdge(g.vertices[0], g.vertices[1], 4)
    g.addEdge(g.vertices[0], g.vertices[7], 8)

    g.addEdge(g.vertices[1], g.vertices[2], 8)
    g.addEdge(g.vertices[1], g.vertices[7], 11)

    g.addEdge(g.vertices[2], g.vertices[3], 7)
    g.addEdge(g.vertices[2], g.vertices[8], 2)
    g.addEdge(g.vertices[2], g.vertices[5], 4)

    g.addEdge(g.vertices[3], g.vertices[4], 9)
    g.addEdge(g.vertices[3], g.vertices[5], 14)

    g.addEdge(g.vertices[4], g.vertices[5], 10)

    g.addEdge(g.vertices[5], g.vertices[6], 2)

    g.addEdge(g.vertices[6], g.vertices[8], 6)
    g.addEdge(g.vertices[6], g.vertices[7], 1)
    
    g.addEdge(g.vertices[7], g.vertices[8], 7)

    mst = prim(g, g.root.id)
    print(mst)