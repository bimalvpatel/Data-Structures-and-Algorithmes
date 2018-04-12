import sys


class Vertex():

    def __init__(self, id):
        self.id = id
        self.visited = False
        self.colour = 'white'
        self.adjacent = {}
        self.distance = sys.maxint
        self.previous = None

    def setVertexId(self, id):
        self.id = id

    def getVertexId(self):
        return self.id

    def setvisited(self):
        self.visited = True

    def setcolour(self, colour):
        self.colour = colour

    def getcolour(self):
        return self.colour

    def setdistance(self, dist):
        self.distance = dist

    def getdistance(self):
        return self.distance

    def setprevious(self, prev):
        self.previous = prev

    def getprevious(self):
        return self.previous

    def getConnections(self):
        return self.adjacent.keys()

    def addNeighbour(self, neighbour, weight):
        self.adjacent[neighbour] = weight

    def getWeight(self, neighbour):
        return self.adjacent[neighbour]

    def __str__(self):
        return str(self.id) + " Connected to: " + str([x.id for x in self.adjacent])


class Graph():

    def __init__(self):
        self.vertlist = {}
        self.numVertices = 0

    def addVertex(self, id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertlist[id] = newVertex
        return newVertex

    def __iter__(self):
        return iter(self.vertlist.values())

    def addEdge(self, frmid, toid, weight):
        if frmid not in self.vertlist:
            self.addVertex(frmid)
        if toid not in self.vertlist:
            self.addVertex(toid)

        self.vertlist[frmid].addNeighbour(self.vertlist[toid], weight)
        # self.vertlist[toid].addNeighbour(self.vertlist[frmid],weight)

    def getVertex(self, id):
        if id in self.vertlist:
            return self.vertlist[id]
        else:
            return None

    def getVertices(self):
        return self.vertlist.keys()

    def getEdges(self):
        edge = []
        for v in self.vertlist.values():
            for w in v.getConnections():
                vid = v.getVertexId()
                wid = w.getVertexId()
                edge.append((vid, wid, v.adjacent[w]))
        return edge


def BFS(G):
    for v in G:
        if (v.getcolour() == 'white'):
            BFSTraversal(G, v.getVertexId())


def BFSTraversal(G, s):
    start = G.getVertex(s)
    start.setdistance(0)
    start.setprevious(None)
    vertqueue = []
    vertqueue.append(start)

    while vertqueue:
        currentVert = vertqueue.pop(0)
        print(currentVert.getVertexId(), currentVert.getdistance())
        for nbr in currentVert.getConnections():
            if nbr.getcolour() == 'white':
                nbr.setcolour('gray')
                nbr.setdistance(currentVert.getdistance() + 1)
                nbr.setprevious(currentVert)
                vertqueue.append(nbr)
        # print("Over")
        currentVert.setcolour('black')


if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addEdge('a', 'b', 1)
    G.addEdge('a', 'c', 1)
    G.addEdge('b', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('e', 'a', 1)
    print 'Graph data:'
    print G.getEdges()

    BFS(G)
