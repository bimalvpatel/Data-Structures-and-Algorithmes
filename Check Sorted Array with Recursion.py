
def checksortedarray(a):
    if len(a) == 1:
        return True
    return a[0] <= a[1] and checksortedarray(a[1:])


if __name__ == "__main__":
    a = map(int,raw_input("Enter Array Elements: ").split())
    print(checksortedarray(a))