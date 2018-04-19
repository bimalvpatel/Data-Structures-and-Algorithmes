import sys

class Vertex():

    def __init__(self,id):
        self.id = id
        self.visited = False
        self.adjacent = {}
        self.distance = sys.maxint
        self.previous = None

    def addNeighbour(self,neighbour,weight):
        self.adjacent[neighbour] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getweight(self,neighbour):
        return self.adjacent[neighbour]

    def setvisited(self):
        self.visited = True

    def getvisited(self):
        return self.visited

    def setVertexId(self,id):
        self.id = id

    def getVertexId(self):
        return self.id

    def setdistance(self,dist):
        self.distance = dist

    def getdistance(self):
        return self.distance

    def setprevious(self,prev):
        self.previous = prev

    def getprevious(self):
        return self.previous

    def __str__(self):
        return str(self.id) + " Connected to: "+str([x.id for x in self.adjacent])


class Graph():

    def __init__(self):
        self.numVertices = 0
        self.vertlist = {}

    def addVertex(self,id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertlist[id] = newVertex
        return newVertex

    def getVertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())

    def getVertex(self,id):
        if id in self.vertlist:
            return self.vertlist[id]
        else:
            return None

    def addEdge(self,frmid,toid,weight):
        if frmid not in self.vertlist:
            self.addVertex(frmid)
        if toid not in self.vertlist:
            self.addVertex(toid)
        self.vertlist[frmid].addNeighbour(self.vertlist[toid],weight)
        #self.vertlist[toid].addNeighbour(self.vertlist[frmid],weight)

    def getEdges(self):
        edge = []
        for v in self.vertlist.values():
            for w in v.getConnections():
                vid = v.getVertexId()
                wid = w.getVertexId()
                edge.append((vid,wid,v.getweight(w)))
        return edge

def DFSTraversal(G):
    for v in G:
        if not v.getvisited():
            v.setdistance(0)
            v.setprevious(None)
            dfs(G,v.getVertexId())

def dfs(G,v):
    start = G.getVertex(v)
    start.setvisited()
    if start.getprevious() != None:
        print("Traversal: " + str(v) + " " + str(start.getdistance()) + " " + str(start.getprevious().getVertexId()))
    for nbr in start.getConnections():
        if not nbr.getvisited():
            nbr.setdistance(start.getdistance()+1)
            nbr.setprevious(start)
            dfs(G,nbr.getVertexId())


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
    DFSTraversal(G)