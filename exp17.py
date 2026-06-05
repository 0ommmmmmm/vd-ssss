def towerofhanoi(n, source, destination, auxiliary):
    if n == 1:
        print("move disk 1 from Source", source, "to destination", destination)
        return
    towerofhanoi(n-1, source, auxiliary, destination)
    print("move disk", n, "from source", source, "to destination", destination)
    towerofhanoi(n-1, auxiliary, destination, source)

n = int(input("Enter the number of disks: "))
towerofhanoi(n, 'A', 'B', 'C')