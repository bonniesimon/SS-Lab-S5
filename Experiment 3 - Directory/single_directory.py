from termcolor import colored

files = []
error = 0


def printDirectory():
    if(len(files) == 0):
        print("--------------------------\n | Empty Directory | \n--------------------------")
    else:
        # print("---------------------------------------\n root directory\n---------------------------------------\n")
        for file in files:
            print(colored(f"{file}", "cyan"), end="   ")
        print('\n')
        # print("\n---------------------------------------\n")

def addFile(fname):
    # fname = input("Enter File name : ")
    if fname not in files:
        files.append(fname)
    else:
        print(colored("Error: File already exist!!\n",'red'))
    
def deleteFile(fname):
    # fname = input("Enter File Name : ")
    if fname not in files:
        print(colored("Error: File doesn't exist!!\n",'red'))
        return
    files.remove(fname)
    

print("Type help to list commands")
while(1):
    print(colored("bonnie@SSlab >> ","blue"), end=" ")
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
        print("Wrong choice!!\n")



