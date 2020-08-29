
# files = ["" for x in range(100)]
files = []


def printDirectory():
    if(len(files) == 0):
        print("--------------------------\n | Empty Directory | \n--------------------------")
    else:
        print("---------------------------------------\n root directory\n---------------------------------------\n")
        for file in files:
            print(file)
            print("    ")
        print("---------------------------------------\n")

def addFile(fname):
    # fname = input("Enter File name : ")
    files.append(fname)
    
def deleteFile(fname):
    # fname = input("Enter File Name : ")
    if fname not in files:
        print("File doesn't exist!!\n")
    

while(1):
    print("Type help to list commands")
    print(">> ")
    choice =input()
    command = choice.split(' ')[0]
    try:
        filename = choice.split(' ')[1]
    except:
        pass
    if(command== "ls"):
        printDirectory()
    elif(command == "touch"):
        addFile(filename)
    elif(command == "rm"):
        deleteFile(filename)
    elif(command == "exit"):
        exit()
    else:
        print("Wrong choice mishter!!\n")



