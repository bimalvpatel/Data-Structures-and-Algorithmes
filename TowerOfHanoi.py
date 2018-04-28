def TowerOfHanoi(n,from_rod,to_rod,aux):
    if n == 1:
        print("Move 1 disk from "+str(from_rod)+" to "+str(to_rod))
        return
    TowerOfHanoi(n-1,from_rod,aux,to_rod)
    print("Move "+ str(n)+ " disk from "+str(from_rod)+" to "+str(to_rod))
    TowerOfHanoi(n-1,aux,to_rod,from_rod)

if __name__ == "__main__":
    TowerOfHanoi(int(raw_input("Enter Disks to Move: ")),'A','C','B')