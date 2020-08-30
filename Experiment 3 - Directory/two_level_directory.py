from termcolor import colored


class Directory:

    def __init__(self, name, level):
        self.name = name
        self.files = []
        self.directories = []
        self.level = level

    def getName(self):
        return self.name

    def touch(self, filename):
        self.files.append(filename)

    def rm(self, filename):
        if filename in self.files:
            self.files.remove(filename) 
            return
        print("Error : File doesn't exists")
    
    def mkdir(self, directory_name):
        next_level = self.level + 1
        if(next_level < 3):
            self.directories.append(Directory(directory_name,next_level))
        else:
            print("Error: Only two levels are possible")

    def rmdir(self, directory_name):
        found = 0
        for directory in self.directories:
            if (directory.name == directory_name):
                found = 1
                self.directories.remove(directory)
                break
        if(not found):
            print("Error: Directory doesn't exist")

    def ls(self):
        for file in self.files:
            print(file, end="  ")
        for directory in self.directories:
            print(directory.name, end="  ")
        print()
    
    def open(self, directory_name):
        found = 0
        for directory in self.directories:
            if (directory.name == directory_name):
                found = 1
                directory.ls()
                break
        if(not found):
            print("Error: Directory doesn't exist")

    def touchInto(self, directory_name, filename):
        found = 0
        for directory in self.directories:
            if (directory.name == directory_name):
                found = 1
                directory.touch(filename)
                break
        if(not found):
            print("Error: Directory doesn't exist")

    



def main():
    root = Directory("bin", 1)
    print("Type help to list commands")    
    while(1):
        print(colored("bonnie@SSlab >> ","blue"), end=" ")
        choice =input()
        command = choice.split(' ')[0]
        try:
            name = choice.split(' ')[1]
            option = choice.split(' ')[2]
        except:
            pass
        if(command == 'mkdir'):
            root.mkdir(name)
        elif(command == "touch"):
            root.touch(name)
        elif(command == "ls"):
            root.ls()
        elif(command == "open"):
            root.open(name)
        elif(command == "touchInto"):
            root.touchInto(name, option)
        elif(command == "rm"):
            root.rm(name)
        elif(command == "rmdir"):
            root.rmdir(name)
        elif(command == "help"):
            print("----------------------------------------\nman page\n----------------------------------------")
            print("%-35s %-38s" % ("ls", "List Files"))
            print("%-35s %-38s" % ("touch <filename>", "Create a file"))
            print("%-35s %-38s" % ("mkdir <directory>", "Create a directory"))
            print("%-35s %-38s" % ("rm <filename>", "Delete a file"))
            print("%-35s %-38s" % ("rmdir <directory>", "Delete a directory"))
            print("%-35s %-38s" % ("open <directory>", "list contens of directory"))
            print("%-35s %-38s" % ("touchInto <directory> <filename>", "Create file inside directory"))
            print("%-35s %-38s" % ("exit", "Exit the shell"))
            print("----------------------------------------\n")
        elif(command == "exit"):
            exit()
        else:
            print("Error: Wrond Command")

main();