import sys

class Vertex():

    def __init__(self,id):
        self.id = id
        self.visited = False
        self.adjacent = {}
        self.previous = None
        self.distance = sys.maxint

    def addNeighbour(self,neighbour,weight):
        self.adjacent[neighbour] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbour):
        return self.adjacent[neighbour]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph():

    def __init__(self):
        self.numVertices = 0
        self.vertlist = {}

    def addVertex(self,id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertlist[id] = newVertex
        return newVertex

    def __iter__(self):
        return iter(self.vertlist.values())

    def getVertex(self,id):
        if id in self.vertlist:
            return self.vertlist[id]
        else:
            return None

    def addEdge(self,frmid,toid,weight=0):
        if frmid not in self.vertlist:
            self.addVertex(frmid)
        if toid not in self.vertlist:
            self.addVertex(toid)
        self.vertlist[frmid].addNeighbour(self.vertlist[toid],weight)
        self.vertlist[toid].addNeighbour(self.vertlist[frmid],weight)

    def getvertices(self):
        return self.vertlist.keys()

    def getEdges(self):
        edge = []
        for v in self.vertlist.values():
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edge.append((vid,wid,v.getWeight(w)))
        return edge


if __name__ == "__main__":
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a', 'b', 4)
    G.addEdge('a', 'c', 1)
    G.addEdge('c', 'b', 2)
    G.addEdge('b', 'e', 4)
    G.addEdge('c', 'd', 4)
    G.addEdge('d', 'e', 4)

    print 'Graph data:'
    print G.getEdges()