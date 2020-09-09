import sys


def printArray(arr, length=0):
    if(length == 1):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
        print( end="\n -----------------------\n")
        return
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
    print( end="\n -----------------------\n")
    return

def setNeedArray(allocation, maximum):
    p = len(allocation)
    r = len(allocation[0])
    need = [[0 for j in range(r)] for i in range(p)]
    for i in range(p): 
        for j in range(r): 
            need[i][j] = maximum[i][j] - allocation[i][j]
    return need;

def compare(need, work):
    for j in range(len(need)):
        if(need[j] > work[j]):
            return 0;
            break
    return 1;


def safety_algorithm(allocation, available, need):
    p = len(allocation)
    r = len(available)
    count = 0
    finished_process = 0
    work = available[:]
    finish = [0 for i in range(p)]
    i = 0
    while(count < p):
        isOneProcessAllocated = False
        for process in range(p):
            if(finish[process] == 0 ):
                isLess = compare(need[process], work)
                if(isLess):
                    for i in range(r):
                        work[i] += allocation[process][i]
                    finish[process] = 1
                    count +=1
                    isOneProcessAllocated = True
        
        if(not isOneProcessAllocated):
            print("System not in safe state!")
            exit()
    
    print("System is in safe state")
    exit()



def main_static_input():
    available = [3, 3, 2]
    allocation = [[0, 1, 0], [2, 0, 0], 
             [3, 0, 2], [2, 1, 1], 
             [0, 0, 2]]  
    maximum = [[7, 5, 3], [3, 2, 2], 
            [9, 0, 2], [2, 2, 2], 
            [4, 3, 3]] 
        

    need = setNeedArray(allocation, maximum)
    safety_algorithm(allocation, available, need)

def main_dynamic_input():
    process = int(input("Enter number of process : "))
    resources = int(input("Enter number of resources : "))
    available = []
    maximum = []
    allocation = []
    print("Enter Available array: ")
    for i in range (1):
        available = list(map(int, input().split()))
        

    print("Enter the allocation array : ")
    for i in range(0, process):
        x = [int(x) for x in input().split()] 
        allocation.append(x)

    print("Enter the max array : ")
    for i in range(0, process):
        x = [int(x) for x in input().split()] 
        maximum.append(x)

    need = setNeedArray(allocation, maximum)
    safety_algorithm(allocation, available, need)



def test():
    resources = 4
    output = compare([0,0,0,10], [1,1,2, 1])
    print(output)


if(len(sys.argv) > 1 and sys.argv[1] == 'test'):
    test()
elif(len(sys.argv) > 1 and sys.argv[1] == "input"):
    main_dynamic_input()
else:
    main_static_input()