'''
def CountingSort(A,k):
    B = [0 for el in A]
    C = [0 for i in range(k+1)]

    for j in range(len(A)):
        C[A[j]] += 1

    for j in range(1,k+1):
        C[j] += C[j-1]

    for j in range(len(A)):
        tmp = A[j]
        tmp1 = C[tmp] - 1
        B[tmp1] = tmp
        C[tmp] -= 1
    return B
'''
def CountingSort(A,k):
    C = [0 for i in range(k+1)]
    for j in A:
        C[j] += 1
    i = 0
    for a in range(k+1):
        for j in range(C[a]):
            A[i] = a
            i += 1
    return A


if __name__ == "__main__":
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    print(CountingSort(A, 1000))