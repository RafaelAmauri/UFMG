class Vertex:
    def __init__(self, vertexId: int, value=0) -> None:
        """
            Input: 
                id: a unique integer used for identifying the vertex
                value (optional): the value that the vertex holds. Generally an int, but could be a float, str, whatever.

            Output:
                a Vertex object
        """ 

        self.id        = vertexId
        self.value     = value
        self.neighbors = dict()
        

    def copy(self):
        vertexCopy = Vertex(self.id, self.value)
        for neighborId, neighborWeight in self.neighbors.items():
            vertexCopy.neighbors[neighborId] = neighborWeight

        return vertexCopy

    
    def __repr__(self) -> str:
        return f"ID = {self.id}, Value = {self.value}"