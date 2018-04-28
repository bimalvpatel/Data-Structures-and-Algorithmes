'''longest path of connected cells'''


def pathFinder(Matrix,position,size):
    if position == (size-1,size-1):
        return [position]
    x,y = position
    #print(position)
    if x+1 < size and Matrix[x+1][y] == 1:
        return [(x,y)] + pathFinder(Matrix,(x+1,y),size)
    if y+1 < size and Matrix[x][y+1] == 1:
        return [(x,y)] + pathFinder(Matrix,(x,y+1),size)
    return [(x,y)]
if __name__ == "__main__":
    Matrix = [[1, 1, 0, 1, 1], [0, 1, 0, 1, 1], [0, 1, 0, 1, 1], [0, 1, 0, 0, 1], [1, 1, 1, 0, 1]]
    maxlength = 0
    for i in range(5):
        for j in range(5):
            if Matrix[i][j] == 1:
                seen = pathFinder(Matrix,(i,j),len(Matrix))
                #print(seen)
                maxlength = max(maxlength,len(seen))
    print(maxlength)
