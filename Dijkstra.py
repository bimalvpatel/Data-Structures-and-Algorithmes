import sys

class Vertex():

    def __init__(self,name):
        self.name = name
        self.visited = False
        self.distance = sys.maxint
        self.adjacent = {}
        self.previous = None

    def addNeighbour(self,neighbour,weight):
        self.adjacent[neighbour] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def setVertexName(self,name):
        self.name = name

    def getVertexName(self):
        return self.name

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

    def getweight(self,neighbour):
        return self.adjacent[neighbour]

    def __str__(self):
        return str(self.name) + " Connected to: " + str([x.name for x in self.adjacent])

class Graph():

    def __init__(self):
        self.numvertices = 0
        self.vertlist = {}

    def __iter__(self):
        return iter(self.vertlist.values())

    def addVertex(self,name):
        self.numvertices += 1
        newVertex = Vertex(name)
        self.vertlist[name] = newVertex
        return newVertex

    def getVertex(self,name):
        if name in self.vertlist:
            return self.vertlist[name]
        else:
            return None

    def addEdge(self,frmname,toname,weight):
        if frmname not in self.vertlist:
            self.addVertex(frmname)
        if toname not in self.vertlist:
            self.addVertex(toname)
        self.vertlist[frmname].addNeighbour(self.vertlist[toname],weight)

    def getVertices(self):
        return self.vertlist.keys()

    def getEdges(self):
        edge = []
        for v in self.vertlist.values():
            for w in v.getConnections():
                vid = v.getVertexName()
                wid = w.getVertexName()
                edge.append((vid,wid,v.getweight(w)))
        return edge

def dijkstra(G,source):
    sourcevertex = G.getVertex(source)
    sourcevertex.setdistance(0)
    sourcevertex.setprevious(None)
    verticeslist = []
    verticeslist.append(sourcevertex)
    while len(verticeslist) > 0:
        current = verticeslist.pop(0)
        for nbr in current.getConnections():
            if nbr.getdistance() > current.getdistance() + current.getweight(nbr):
                nbr.setdistance(current.getdistance()+current.getweight(nbr))
                nbr.setprevious(current)
                verticeslist.append(nbr)

def shortest(G,target):
    targetvertex = G.getVertex(target)
    result = target
    while targetvertex.getprevious() is not None:
        targetvertex = targetvertex.getprevious()
        result = str(result) + " " + str(targetvertex.getVertexName())
    return result

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

    dijkstra(G,'a')
    for v in G:
        print(str(v.getVertexName()) + " : "+str(v.getdistance()))

    print(shortest(G,'e'))