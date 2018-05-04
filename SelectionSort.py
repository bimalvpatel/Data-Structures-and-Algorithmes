def SelectionSort(A):
    for i in range(len(A)-1):
        least = i
        for j in range(i+1,len(A)):
            if A[j] < A[least]:
                least = j
        A[least],A[i] = A[i],A[least]


if __name__ == "__main__":
    A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    SelectionSort(A)
    print(A)