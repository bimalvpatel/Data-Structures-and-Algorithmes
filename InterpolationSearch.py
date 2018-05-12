def InterpolationSearch(A,ele):
    low = 0
    high = len(A)-1
    while A[low] <= ele and A[high] >= ele:
        mid = low + (((ele-A[low])*(high-low))/(A[high]-A[low]))
        if A[mid] == ele:
            return mid
        elif A[mid] < ele:
            low = mid + 1
        elif A[mid] > ele:
            high = mid -1
    return -1


if __name__ == "__main__":
    A = [-30, -16, -9, 3, 10, 11, 18, 22, 54, 84, 105]
    print InterpolationSearch(A, -10)