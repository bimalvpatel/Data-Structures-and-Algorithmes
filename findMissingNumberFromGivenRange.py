'''
A contains only positive elements
A is editable
range is also in positive numbers
'''


def findMissingNumberFromGivenRange(A,X,Y):
    n = len(A)
    for i in range(n):
        if A[abs(A[i])-X] > 0:
            A[abs(A[i])-X] *= -1
    for i in range(n):
        if A[i] > 0:
            return i + X

if __name__ == "__main__":
    A = [10, 16, 14, 12, 11, 10, 13 , 15, 17, 12, 19]
    print findMissingNumberFromGivenRange(A, 10, 20)