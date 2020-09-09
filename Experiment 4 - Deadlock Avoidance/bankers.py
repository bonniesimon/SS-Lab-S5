import sys


process, resources = 0, 0


def printArray(arr, length=0):
    if(length == 1):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
        return
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
    return

def setNeedArray(allocation, maximum):
    need = []
    tempArr=[]
    for i in range(len(allocation)):
        for j in range(len(allocation[0])):
            tempArr.append(maximum[i][j] - allocation[i][j])
        need.append(tempArr)
    return need;

def compare(need, work):
    if(need[0] <= work[0] and need[1] <= work[1] and need[2] <= work[2]):
        return 1;
    return 0;


def safety_algorithm(allocation, available, need):
    work = available[:]
    finish = [0 for i in range(len(allocation))]
    i = 0
    while(0 in finish):
        if(1):
            pass





def main():
    process = int(input("Enter number of process : "))
    resources = int(input("Enter number of resources : "))
    available = []
    maximum = []
    allocation = []
    need = []
    for i in range (1):
        available = list(map(int, input("Enter Available Array : ").split()))

    print("Enter the allocation array : ")
    for i in range(0, process):
        # for j in range(0, resources):
            # allocation[i] = list(map(int, input("Enter elements : ").split()))
            # available[i][j] = int(input())
        x = [int(x) for x in input().split()] 
        allocation.append(x)

    print("Enter the max array : ")
    for i in range(0, process):
        x = [int(x) for x in input().split()] 
        maximum.append(x)

    need = setNeedArray(allocation, maximum)
    safety_algorithm(allocation, available, need)



def test():
    output = compare([2,1,0], [1,1,2])
    print(output)


if(sys.argv[1] == 'test'):
    test()
else:
    main()