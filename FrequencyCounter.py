'''
A contains elements from 1 to n
A is editable
'''

def frequencyCounter(A):
    pos = 0
    n = len(A)
    maxele = 0
    while pos < n:
        expectedpos = A[pos] - 1
        if maxele < A[pos]:
            maxele = A[pos]
        if A[pos] > 0 and A[expectedpos] > 0:
            A[pos], A[expectedpos] = A[expectedpos], A[pos]
            A[expectedpos] = -1
        elif A[pos] > 0:
            A[expectedpos] -= 1
            A[pos] = 0
            pos += 1
        else:
            pos += 1
        #print(A)
    for i in range(1,maxele+1):
        print i ,"--->",abs(A[i-1])

if __name__ == "__main__":
    A = [10, 1, 1, 4, 7, 6, 5, 2,2, 1,3, 2, 9]
    frequencyCounter(A)