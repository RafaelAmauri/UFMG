from include.vertex import Vertex

class Graph:
    def __init__(self, root: Vertex) -> None:
        """
            Input:
                root: a Vertex object
            
            Output:
                None
        """
        self.root     = root
        self.numEdges = 0
        self.vertices = {
                root.id: root
            }
    

    def addVertex(self, v: Vertex) -> None:
        """
            Input:
                v: a Vertex object
            
            Output:
                None
        """

        self.vertices[v.id] = v
    

    def addEdge(self, src: Vertex, dest: Vertex, weight: int) -> None:
        """
            Adds a connection between the src and the destination vertices.

            This function considers that the graph is undirected.

            It was originally a method of the Vertex class, but I moved it here to
            make it possible to count how many edges are in a graph.

            Input:
                dest: a Vertex object
                weight: an integer representing the weight of the edge connecting self and dest
            
            Output:
                None
        """
        if dest.id not in src.neighbors:
            src.neighbors[dest.id] = weight
            dest.neighbors[src.id] = weight

            self.numEdges += 1


    def removeEdge(self, src, dest: 'Vertex') -> None:
        if src.id in dest.neighbors:
            del src.neighbors[dest.id]
            del dest.neighbors[src.id]

            self.numEdges -= 1


    def __repr__(self) -> str:
        printedPairs = set()
        returnStr    = ""
        for vertexId, vertex in self.vertices.items():
            for neighborId, neighborWeight in vertex.neighbors.items():
                if (neighborId, vertexId) not in printedPairs:
                    returnStr += f"{vertexId} -- {neighborId} // W = {neighborWeight}\n"
                    printedPairs.add((vertexId, neighborId))
        
        return returnStr