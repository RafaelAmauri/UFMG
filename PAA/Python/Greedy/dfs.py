from include.graph import Graph
from include.vertex import Vertex


def depthFirstSearch(graph: Graph, srcId: int, destId: int) -> list:
    """
        Performs a search in graph for the vertex with id destId.

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
            
            for neighborId in currentVertex.neighbors:
                if neighborId not in (list(visitedVertices) + stack):
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


def dfsCountConnectedComponents(graph: Graph) -> int:

    visitedVertices = set()
    nComponents     = 0

    for vId in graph.vertices.keys():
        stack           = [vId]
        if vId not in visitedVertices:
            while stack:
                currentVertexId = stack.pop(0)

                visitedVertices.add(currentVertexId)
                currentVertex = graph.vertices[currentVertexId]
                for neighborId in currentVertex.neighbors:
                    if neighborId not in visitedVertices:
                        stack.insert(0, neighborId)

            nComponents += 1
        else:
            stack = []

    return nComponents


if __name__ == '__main__':
    vertices = [Vertex(i) for i in range(0, 11)]

    g = Graph(vertices[0])
    for v in vertices:
        g.addVertex(v)

    g.addEdge(vertices[0], vertices[1], 0)
    g.addEdge(vertices[0], vertices[2], 0)
    g.addEdge(vertices[1], vertices[4], 0)
    g.addEdge(vertices[2], vertices[3], 0)
    g.addEdge(vertices[4], vertices[5], 0)
    g.addEdge(vertices[5], vertices[6], 0)
    g.addEdge(vertices[7], vertices[8], 0)
    g.addEdge(vertices[9], vertices[10], 0)

    print(depthFirstSearch(g, g.root.id, 5))