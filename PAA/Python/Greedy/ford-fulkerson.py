from include.digraph import DiGraph
from include.vertex import Vertex

def updateFlow(graph: DiGraph, srcId: int, destId: int, bottleneck):
    if destId not in graph.vertices[srcId].neighbors:
        graph.vertices[srcId].neighbors[destId] = 0

    graph.vertices[srcId].neighbors[destId] += bottleneck


def breadthFirstSearch(graph: DiGraph, srcId: int, destId: int) -> list:
    """
        Performs a search in graph for the vertex with id destId.
        Modified to be used with Ford Fulkerson.

        Input:
            graph: a graph element
            srcId: the ID of the vertex where the search will start from
            destId: the ID of the vertex to be found
        
        Output:
            path: a list with a path from srcId to destId
    """

    stack           = [srcId]
    visitedVertices = set()
    parent          = {}
    notFound        = True

    while stack and notFound:
        currentVertexId = stack.pop(0)
        if currentVertexId == destId:
            notFound = False
            continue
        
        else:
            visitedVertices.add(currentVertexId)
            currentVertex = graph.vertices[currentVertexId]
            
            for neighborId, neighborWeight in currentVertex.neighbors.items():
                if neighborId not in visitedVertices and neighborWeight > 0 and neighborId not in stack:
                    stack.append(neighborId)
                    parent[neighborId] = currentVertexId
    
    path = []
    if not notFound:
        currentVertexId = destId
        while currentVertexId != srcId:
            path.insert(0, currentVertexId)
            currentVertexId = parent[currentVertexId]
        path.insert(0, srcId)

    return path


def depthFirstSearch(graph: DiGraph, srcId: int, destId: int) -> list:
    """
        Performs a search in graph for the vertex with id destId. 
        Modified to be used with Ford Fulkerson.

        Input:
            graph: a DiGraph element
            srcId: the ID of the vertex where the search will start from
            destId: the ID of the vertex to be found
        
        Output:
            path: a list with a path from srcId to destId
    """

    stack           = [srcId]
    visitedVertices = set()
    parent          = {}
    notFound        = True

    while stack and notFound:

        currentVertexId = stack.pop(0)

        if currentVertexId == destId:
            notFound = False
            continue
        
        else:
            visitedVertices.add(currentVertexId)
            currentVertex = graph.vertices[currentVertexId]
            
            for neighborId, neighborWeight in currentVertex.neighbors.items():
                if neighborId not in visitedVertices and neighborWeight > 0 and neighborId not in stack:
                    stack.insert(0, neighborId)
                    parent[neighborId] = currentVertexId
    
    path = []
    if not notFound:
        currentVertexId = destId
        while currentVertexId != srcId:
            path.insert(0, currentVertexId)
            currentVertexId = parent[currentVertexId]
        path.insert(0, srcId)

    return path


def fordFulkerson(graph: DiGraph, srcId: int, sinkId: int):
    maxFlow = 0
    
    # Create vertices in the Flow Graph
    flowGraph = DiGraph(Vertex(srcId))
    for vId in graph.vertices.keys():
        flowGraph.addVertex(Vertex(vId))

    # Create residual graph
    residualGraph = graph.deepcopy()

    # Find augmenting paths until no more are available
    path = breadthFirstSearch(residualGraph, srcId, sinkId)
    while(len(path) != 0):
        bottleneck = float('inf')
        # Find bottleneck capacity along the path
        for i in range(0, len(path)-1):
            neighborWeight = residualGraph.vertices[path[i]].neighbors[path[i+1]]
            bottleneck     = min(neighborWeight, bottleneck)

        maxFlow += bottleneck

        # Update residual capacities
        for i in range(0, len(path)-1):
            currentVertexId  = path[i]
            neighborVertexId = path[i+1]

            updateFlow(flowGraph, currentVertexId, neighborVertexId, bottleneck)
            updateFlow(flowGraph, neighborVertexId, currentVertexId, -bottleneck)

            updateFlow(residualGraph, currentVertexId, neighborVertexId, -bottleneck)
            updateFlow(residualGraph, neighborVertexId, currentVertexId, bottleneck)

        path = breadthFirstSearch(residualGraph, srcId, sinkId)

    return maxFlow


if __name__ == '__main__':
    vertices = [Vertex(i) for i in range(0, 6)]

    graph = DiGraph(vertices[0])
    [graph.addVertex(v) for v in vertices]

    # This graph can be visualized in https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
    edges = [ (0, 1, 16), (0, 2, 13), (1, 3, 12), (1, 2, 10), (2, 1, 4), (2, 4, 14), (3, 5, 20), (3, 2, 9), (4, 5, 4), (4, 3, 7) ]
    
    for src, dest, weight in edges:
        graph.addEdge(vertices[src], vertices[dest], weight)

    print(fordFulkerson(graph, 0, 5))