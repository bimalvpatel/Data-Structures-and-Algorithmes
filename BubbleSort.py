def BubbleSort(A):
    k = 0
    for i in range(len(A)):
        swapped = 0
        for j in range(len(A)-i-1):
            k += 1
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                swapped = 1
        if swapped == 0:
            break
    print(k)


if __name__ == "__main__":
    A = [127, 220, 246, 277, 321, 454, 534, 565, 933]
    BubbleSort(A)
    print(A)