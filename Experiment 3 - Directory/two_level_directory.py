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
    
    def mkdir(self, directory_name):
        current_level = self.level + 1
        self.directories.append(Directory(directory_name, current_level))

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

    def touchInside(self, directory_name, filename):
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
    current_dir = root
    root.touch('main.py') 
    root.touch('fast.py')
    root.mkdir('second')
    root.ls()
    root.touchInside('second', 'project1')
    root.open('second')
    print()


main();