from include.digraph import DiGraph
from include.vertex import Vertex

def dfs(g, startVertexId, visitedVertices, sortedGraph):
    
    visitedVertices.add(startVertexId)
    for neighborId in g.vertices[startVertexId].neighbors:
        if neighborId not in visitedVertices:
            dfs(g, neighborId, visitedVertices, sortedGraph)
    
    sortedGraph.insert(0, startVertexId)


def topologicalSort(g: DiGraph) -> list:
    """
    This is the topological sorting of a graph.

    Inputs:
        g: a Graph object
    Outputs:
        sortedGraph: a list with the elements of the graph topologically sorted
    """

    sortedGraph     = []
    visitedVertices = set()
    for vertexId in g.vertices.keys():
        if vertexId not in visitedVertices:
            dfs(g, vertexId, visitedVertices, sortedGraph)
    

    print(sortedGraph)


if __name__ == '__main__':
    vertices = [Vertex(i) for i in range(0, 6)]

    g = DiGraph(vertices[0])
    for v in vertices:
        g.addVertex(v)

    # This graph can be visualized in https://www.geeksforgeeks.org/topological-sorting/
    edges = [ (5, 0), (4, 0), (4, 1), (5, 2), (2, 3), (3, 1) ]

    for srcId, destId in edges:
        g.addEdge(vertices[srcId], vertices[destId], 0)

    print(topologicalSort(g))