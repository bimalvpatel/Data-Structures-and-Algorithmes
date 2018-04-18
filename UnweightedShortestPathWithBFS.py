import sys

class Vertex():

    def __init__(self,name):
        self.name = name
        self.visited = False
        self.distance = -1
        self.adjacent = {}
        self.previous = None

    def addNeighbour(self,neighbour,weight = 0):
        self.adjacent[neighbour] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getVertexName(self):
        return self.name

    def setVertexName(self,name):
        self.name = name

    def setVisited(self):
        self.visited = True

    def getdistance(self):
        return self.distance

    def setdistance(self,dist):
        self.distance = dist

    def getprevious(self):
        return self.previous

    def setprevious(self,prev):
        self.previous = prev

    def __str__(self):
        return str(self.name) + " Connected To: " + str([x.name for x in self.adjacent])

class Graph():

    def __init__(self):
        self.vertlist = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertlist.values())

    def addVertex(self,name):
        self.numVertices += 1
        newVertex = Vertex(name)
        self.vertlist[name] = newVertex
        return newVertex

    def getVertex(self,name):
        if name in self.vertlist:
            return self.vertlist[name]
        else:
            return None

    def addEdge(self,frmname,toname):
        if frmname not in self.vertlist:
            self.addVertex(frmname)
        if toname not in self.vertlist:
            self.addVertex(toname)
        self.vertlist[frmname].addNeighbour(self.vertlist[toname])

    def getVertices(self):
        return self.vertlist.keys()

    def getEdges(self):
        edge = []
        for v in self.vertlist.values():
            for w in v.getConnections():
                vid = v.getVertexName()
                wid = w.getVertexName()
                edge.append((vid,wid))
        return edge

def UnweightedShortestPath(G, source):
    vertices = []
    vertices.append(source)
    currentVertex = G.vertlist[source]
    currentVertex.setdistance(0)
    currentVertex.setprevious(None)
    while len(vertices) > 0:
        currentVertex = G.vertlist[vertices.pop(0)]
        for nbr in currentVertex.getConnections():
            if nbr.getdistance() == -1:
                nbr.setdistance(currentVertex.getdistance()+1)
                nbr.setprevious(currentVertex)
                vertices.append(nbr.getVertexName())
    for v in G.vertlist.values():
        print str(source) + " to " + str(v.getVertexName()) + " --> " + str(v.getdistance())

if __name__ == "__main__":
    G = Graph()
    G.addVertex('A')
    G.addVertex('B')
    G.addVertex('C')
    G.addVertex('D')
    G.addVertex('E')
    G.addVertex('F')
    G.addVertex('G')
    G.addVertex('H')
    G.addVertex('I')
    G.addEdge('A', 'B')
    G.addEdge('A', 'C')
    G.addEdge('A', 'G')
    G.addEdge('A', 'E')
    G.addEdge('B', 'C')
    G.addEdge('C', 'G')
    G.addEdge('D', 'E')
    G.addEdge('D', 'F')
    G.addEdge('F', 'H')
    G.addEdge('E', 'H')
    G.addEdge('H', 'I')
    print 'Graph data:'
    print G.getEdges()
    UnweightedShortestPath(G, 'A')
