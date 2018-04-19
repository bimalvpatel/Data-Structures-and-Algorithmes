import sys

class Vertex():

    def __init__(self,name):
        self.name = name
        self.visited = False
        self.distance = sys.maxint
        self.adjacent = {}
        self.previous = None

    def addNeighbour(self,neighbour,weight = 0):
        self.adjacent[neighbour] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getWeight(self,neighbour):
        return self.adjacent[neighbour]

    def getVertexName(self):
        return self.name

    def setVertexName(self,name):
        self.name = name

    def setvisited(self):
        self.visited = True

    def getvisited(self):
        return self.visited

    def setdistance(self,dist):
        self.distance = dist

    def getdistance(self):
        return self.distance

    def setprevious(self,prev):
        self.previous = prev

    def getprevious(self):
        return self.previous

    def __str__(self):
        return str(self.name) + " Connected To: "+str([x.name for x in self.adjacent])

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
        return  newVertex

    def getVertex(self,name):
        if name in self.vertlist:
            return self.vertlist[name]
        else:
            return None

    def getVertices(self):
        return self.vertlist.keys()

    def addEdge(self,frmname,toname,weight=0):
        if frmname not in self.vertlist:
            self.addVertex(frmname)
        if toname not in self.vertlist:
            self.addVertex(toname)

        self.vertlist[frmname].addNeighbour(self.vertlist[toname],weight)

    def getEdges(self):
        edge = []
        for v in self.vertlist.values():
            for w in v.getConnections():
                edge.append((v.getVertexName(),w.getVertexName()))
        return edge

def bfstraversal(G,s):
    global maxlengthpath
    pathLength = 0
    start = G.getVertex(s)
    start.setdistance(0)
    start.setprevious(None)
    vertqueue = []
    vertqueue.append(start)
    vertqueue.append(None)
    while len(vertqueue) > 0:
        currentVert = vertqueue.pop(0)
        if currentVert == None:
            print(pathLength)
            pathLength += 1
            if len(vertqueue) > 0:
                vertqueue.append(None)
            continue
        print(currentVert.getVertexName())
        for nbr in currentVert.getConnections():
            if not nbr.getvisited():
                nbr.setvisited()
                nbr.setdistance(currentVert.getdistance()+1)
                nbr.setprevious(currentVert)
                vertqueue.append(nbr)
    if pathLength > maxlengthpath:
        maxlengthpath = pathLength

maxlengthpath = 0
def LongestPathInDAG(G):
    for v in G:
        if not v.getvisited():
            bfstraversal(G,v.getVertexName())
    return maxlengthpath

if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addEdge('a', 'b', 1)
    G.addEdge('b', 'c', 1)
    G.addEdge('a', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'f', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('d', 'g', 1)
    G.addEdge('e', 'f', 1)
    G.addEdge('e', 'h', 1)
    G.addEdge('f', 'i', 1)
    G.addEdge('g', 'h', 1)
    G.addEdge('h', 'i', 1)
    print 'Graph data:'
    print G.getEdges()

    print(LongestPathInDAG(G))