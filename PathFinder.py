'''
Path finder from each cell which contains 1 to last cell
'''


def pathfinder(Matrix,position,size):
    if position == (size-1,size-1):
        return [position]
    x,y = position
    if x+1 < size and Matrix[x+1][y] == 1:
        a = pathfinder(Matrix,(x+1,y),size)
        if a != None:
            return [(x,y)]+a
    if y+1 < size and Matrix[x][y+1] == 1:
        b = pathfinder(Matrix,(x,y+1),size)
        if b!= None:
            return [(x,y)]+b
    if x+1 < size and y+1 < size and Matrix[x+1][y+1] == 1:
        c = pathfinder(Matrix,(x+1,y+1),size)
        if c != None:
            return [(x,y)] + c

if __name__ == "__main__":
    Matrix = [[1, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if Matrix[i][j] == 1:
                print(pathfinder(Matrix,(i,j),len(Matrix)))