import sys

class Vertex():

    def __init__(self,name):
        self.name = name
        self.visited = False
        self.inDegree = 0
        self.outDegree = 0
        self.distance = sys.maxint
        self.adjacent = {}
        self.previous = None

    def addNeighbour(self,neighbour,weight = 0):
        self.adjacent[neighbour] = weight

    def getweight(self,neighbour):
        return self.adjacent[neighbour]

    def getConnections(self):
        return self.adjacent.keys()

    def setvisited(self):
        self.visited = True

    def getVertexName(self):
        return self.name

    def setVertexName(self,name):
        self.name = name

    def getdistance(self):
        return self.distance

    def setdistance(self,dist):
        self.distance = dist

    def getprevious(self):
        return self.previous

    def setprevious(self,prev):
        self.previous = prev

    def getInDegree(self):
        return self.inDegree

    def setInDegree(self,inDegree):
        self.inDegree = inDegree

    def __str__(self):
        return str(self.name) + " Connected To: " + str([x.name for x in self.adjacent])

class Graph():

    def __init__(self):
        self.vertlist = {}
        self.numVertices = 0

    def addVertex(self,name):
        self.numVertices += 1
        newVertex = Vertex(name)
        self.vertlist[name] = newVertex
        return newVertex

    def __iter__(self):
        return iter(self.vertlist.values())

    def getVertex(self,name):
        if name in self.vertlist:
            return self.vertlist[name]
        else:
            return None

    def addEdge(self,frmname,toname,weight=0):
        if frmname not in self.vertlist:
            self.addVertex(frmname)
        if toname not in self.vertlist:
            self.addVertex(toname)
        self.vertlist[frmname].addNeighbour(self.vertlist[toname],weight)
        self.vertlist[toname].setInDegree(self.vertlist[toname].getInDegree()+1)

    def getVertices(self):
        return self.vertlist.keys()

    def getEdges(self):
        edge = []
        for v in self.vertlist.values():
            for w in v.getConnections():
                edge.append((v.getVertexName(),w.getVertexName()))
        return edge

def topologicalSort(G):
    topologicalList = []
    topologicalqueue = []
    remainingInDegree = {}

    nodes = G.getVertices()
    for v in G:
        if v.getInDegree() == 0:
            topologicalqueue.append(v)
        else:
            remainingInDegree[v] = v.getInDegree()

    while topologicalqueue:
        #print([x.name for x in topologicalqueue])
        #print([x.name for x in topologicalList])
        currentVertex = topologicalqueue.pop()
        topologicalList.append(currentVertex)
        for nbr in currentVertex.getConnections():
            #print(nbr.getVertexName())
            #print(nbr.getInDegree())
            nbr.setInDegree(nbr.getInDegree()-1)
            #print(nbr.getInDegree())
            if nbr.getInDegree() == 0:
                topologicalqueue.append(nbr)

    if len(nodes) != len(topologicalList):
        return False

    while len(topologicalList):
        print(topologicalList.pop(0).getVertexName())


if __name__ == '__main__':
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
    print(topologicalSort(G))