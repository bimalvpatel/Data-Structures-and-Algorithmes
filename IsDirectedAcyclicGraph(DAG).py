import sys

class Vertex():

    def __init__(self,name):
        self.name = name
        self.visited = False
        self.distance = sys.maxint
        self.adjacent = {}
        self.previous = None
        self.inDegree = 0
        self.outDegree = 0

    def addNeighbour(self,neighbour,weight=0):
        self.adjacent[neighbour] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getWeight(self,neighbour):
        return self.adjacent[neighbour]

    def getVertexName(self):
        return self.name

    def getprevious(self):
        return self.previous

    def setprevious(self,prev):
        self.previous = prev

    def setVertexName(self,name):
        self.name = name

    def __str__(self):
        return str(self.name) + " Connected To: "+str([x.name for x in self.adjacent])

    def setvisited(self):
        self.visited = True

    def getdistance(self):
        return self.distance

    def setdistance(self,dist):
        self.distance = dist

    def getInDegree(self):
        return self.inDegree

    def setInDegree(self,inDegree):
        self.inDegree = inDegree

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
    topologicalQueue = []
    remainingInDegree = {}

    nodes = G.getVertices()
    for v in G:
        if v.getInDegree() == 0:
            topologicalQueue.append(v)
        else:
            remainingInDegree[v] = v.getInDegree()

    while topologicalQueue:
        currentVertex = topologicalQueue.pop()
        topologicalList.append(currentVertex)
        for nbr in currentVertex.getConnections():
            nbr.setInDegree(nbr.getInDegree()-1)
            if nbr.getInDegree() == 0:
                topologicalQueue.append(nbr)

    if len(nodes) != len(topologicalList):
        return False
    else:
        return True

def isDirectedAcyclicGraph(G):

    if topologicalSort(G):
        return True
    else:
        return False


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
    G.addEdge('G', 'A')
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
    print isDirectedAcyclicGraph(G)