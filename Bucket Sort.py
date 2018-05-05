import math
def BucketSort(A):
    code = Hashing(A)
    bucket = [list() for _ in range(code[1])]
    for i in A:
        x = rehashing(i,code)
        bucket[x].append(i)

    for buck in bucket:
        insertionSort(buck)

    j = 0
    for i in range(len(bucket)):
        for k in bucket[i]:
            A[j] = k
            j += 1

    return A

def insertionSort(buck):
    for i in range(1,len(buck)):
        val = buck[i]
        k = i
        while k > 0 and buck[k-1] > val:
            buck[k] = buck[k-1]
            k -= 1
        buck[k] = val

def Hashing(A):
    m = A[0]
    for i in A:
        if m < i:
            m = i
    return [m,int(math.sqrt(len(A)))]

def rehashing(i,code):
    return int(i/code[0] * (code[1]-1))

if __name__ == "__main__":
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    print(BucketSort(A))