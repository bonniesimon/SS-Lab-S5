
# files = ["" for x in range(100)]
files = []


def printDirectory():
    if(len(files) == 0):
        print("--------------------------\n | Empty Directory | \n--------------------------")
    else:
        # print("---------------------------------------\n root directory\n---------------------------------------\n")
        print()
        for file in files:
            print(file, end="   ")
        print("\n")
        # print("\n---------------------------------------\n")

def addFile(fname):
    # fname = input("Enter File name : ")
    files.append(fname)
    
def deleteFile(fname):
    # fname = input("Enter File Name : ")
    if fname not in files:
        print("Error: File doesn't exist!!\n")
        return
    files.remove(fname)
    

print("Type help to list commands")
while(1):
    print("bonnie@SSlab>> ", end=" ")
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
    elif(command == "help"):
        print("----------------------------------------\nman page\n----------------------------------------")
        print("%-20s %-20s" % ("ls", "List Files"))
        print("%-20s %-20s" % ("touch <filename>", "Create a file"))
        print("%-20s %-20s" % ("rm <filename>", "Delete a file"))
        print("%-20s %-20s" % ("exit", "Exit the shell"))
        print("----------------------------------------\n")
    else:
        print("Wrong choice mishter!!\n")



