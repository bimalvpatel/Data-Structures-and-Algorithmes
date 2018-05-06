import math
def radixcount(A):
    RADIX = int(math.sqrt(max(A)))+1

    tmp ,placement = -1,1
    for i in range(2):
        buckets = [[] for _ in range(RADIX)]
        for j in A:
            tmp = j/placement
            buckets[tmp%RADIX].append(j)
        #print(buckets)
        t = 0
        for k in range(len(buckets)):
            for ele in buckets[k]:
                A[t] = ele
                t += 1
        placement *= RADIX
    return A

if __name__ == "__main__":
    A = map(int,raw_input().split())
    print(radixcount(A))