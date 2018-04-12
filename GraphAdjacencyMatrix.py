class Vertex():

    def __init__(self,id):
        self.id = id
        self.visited = False

    def setVertexId(self,id):
        self.id = id

    def getVertexId(self):
        return self.id

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)

''' 
    def addNeighbour(self,neighbour,G):
        G.addEdge(self.id,neighbour)

    def getConnections(self,G):
        return G.adjMatrix(self.id)
'''

class Graph():

    def __init__(self,numVertices):
        self.adjMatrix = [[-1] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for id in range(self.numVertices):
            newVertex = Vertex(id)
            self.vertices.append(newVertex)

    def setVertex(self,vtx,id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexId(id)

    def getVertex(self,id):
        for vtx in range(self.numVertices):
            if id == self.vertices[vtx].getVertexId():
                return vtx
        else:
            return -1

    def addEdge(self,frmid,toid,weight=0):
        if self.getVertex(frmid) != -1 and self.getVertex(toid) != -1:
            self.adjMatrix[self.getVertex(frmid)][self.getVertex(toid)] = weight
            self.adjMatrix[self.getVertex(toid)][self.getVertex(frmid)] = weight

    def getVertices(self):
        vertices = []
        for vtx in range(self.numVertices):
            vertices.append(self.vertices[vtx].getVertexId())
        return vertices

    def printMatrix(self):
        for u in range(self.numVertices):
            row = []
            for v in range(self.numVertices):
                row.append(self.adjMatrix[u][v])
            print row

    def getEdges(self):
        edge = []
        for v in range(self.numVertices):
            for u in range(self.numVertices):
                if self.adjMatrix[v][u] != -1:
                    vid = self.vertices[v].getVertexId()
                    uid = self.vertices[u].getVertexId()
                    edge.append((vid,uid,self.adjMatrix[v][u]))
        return edge

if __name__ == "__main__":
    G = Graph(5)
    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    G.setVertex(4, 'e')
    print 'Graph data:'
    G.addEdge('a', 'e', 10)
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('b', 'e', 40)
    G.addEdge('e', 'd', 50)
    G.addEdge('f', 'e', 60)
    G.printMatrix()
    print G.getEdges()
