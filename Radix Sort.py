def RadixSort(A):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]
        for i in A:
            tmp = i / placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False


        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                A[a] = i
                a += 1
        #print(A)
        # move to next digit
        placement *= RADIX

    return A
if __name__ == "__main__":
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    print(RadixSort(A))