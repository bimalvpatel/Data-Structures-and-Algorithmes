def QuickSort(A,low,high):
    if low < high:
        pivot = Partition(A,low,high)
        QuickSort(A,low,pivot-1)
        QuickSort(A,pivot+1,high)

def Partition(A,low,high):
    pivot = low
    A[pivot],A[high] = A[high],A[pivot]
    for i in range(low,high):
        if A[i] <= A[high]:
            A[i],A[low] = A[low],A[i]
            low += 1
    A[low],A[high] = A[high],A[low]
    return low




if __name__ == "__main__":
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    QuickSort(A, 0, len(A) - 1)
    print(A)