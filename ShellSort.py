def ShellSort(A):
    sublistcount = len(A)/2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            GapShellSort(A,startposition,sublistcount)
        sublistcount /= 2


def GapShellSort(A,start,gap):
    for i in range(start+gap,len(A),gap):
        temp = A[i]
        position = i
        while position >= gap and A[position-gap] > temp:
            A[position] = A[position-gap]
            position = position - gap
        A[position] = temp


if __name__ == "__main__":
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    ShellSort(A)
    print(A)