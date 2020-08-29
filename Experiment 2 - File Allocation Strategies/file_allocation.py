''' 
-----------------------------------------
Exp No:2
Title:File Allocation Strategies
Date:25/08/2020
Author: Bonnie Simon 
Roll no:22
-----------------------------------------
'''

def sequential_allocation():
    l=[0]*50
    c='y'
    
    while(c=='y'):
        start=int(input("Enter starting address\n"))
        filen=int(input("Enter length of file\n"))
        for i in range(start,(start+filen),1):
            if(l[i]!=1):
                l[i]=1
            else:
                print("Block already allocated")
                break

        
        c=input("Do you want to continue?(n,y)\n")
        if(c=='y'):
            continue
        else:
            print(l)
            return

def linked():
    l=[0]*50
    n=int(input("Enter no of allocated blocks\n"))
    for i in range(n):
        bno=int(input("Enter allocated blocks\n"))
        l[bno]=1
    strt=int(input("Enter starting block index\n"))
    lengt=int(input("Enter length:\n"))
    i=strt
    k=strt+lengt
    print('Memory Space is : ')
    if(l[strt]==0):
        while i<k:
            if(l[i]==0):
                l[i]=1
                print(i, " --> 1")
                i+=1
            else:
                print(i,"is already allocated")
                i=i+1
                k=k+1           
    else:
        print("Starting is already allocated")




files = [0]*50
indx = [0]*50
count = 0
prevInd = -1;
def indexed():
        count = 0
        for i in range(n):
            print("Enter next index\n")
            indx[i] = int(input())
            if(files[indx[i]]==0):
                count+=1
        if(count==n):
            for i in range(n):
                files[indx[i]]=1
            print("Allocated\nFile Indexed\n")
            for k in range(n):
                print(ind,"->",indx[k])
        else:
            print("File in index is already allocated")
            print("Enter another file indexed")
            indexed()


while(1):
    print('-----------------------------')
    print("\n1.Sequential allocation\n")
    print("2.Linked allocation\n")
    print("3.Indexed allocation\n")
    print('4.Exit')
    choice=int(input("Enter your choice\n"))
    print('-----------------------------')
    if(choice==1):
        sequential_allocation()
    elif(choice==2):
        linked()
    elif(choice==3):
        ind = int(input("Enter the index block\n"))
        if(ind == prevInd):
            print("Index already allocated!!\n")
            continue
        if(files[ind]==0):
            n = int(input("Enter the number of blocks\n"))
            prevInd = ind
            indexed()
        elif(files[ind]==1):
            print("Index block is allocated")
        else:
            pass
    elif(choice==4):
        print("Exiting..")
        exit()

        

