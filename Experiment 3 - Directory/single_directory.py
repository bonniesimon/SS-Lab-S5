
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

def addFile():
    fname = input("Enter File name : ")
    files.append(fname)
    
def deleteFile():
    fname = input("Enter File Name : ")
    

while(1):
    print("\n\nYou are in the only directory present.\nEnter 1 to show directory\nEnter 2 to add new file\nEnter 3 to delete file\nEnter anything else to exit\n")
    choice = int(input())
    if(choice == 1):
        printDirectory()
    elif(choice == 2):
        addFile()
    elif(choice == 3):
        print("Delete cheyyatte mwonusse\n")
        # deleteFile()
    elif(choice == 4):
        exit()
    else:
        print("Wrong choice mishter!!\n")



