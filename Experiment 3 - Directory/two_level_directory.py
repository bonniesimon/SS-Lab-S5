class Directory:

    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []

    def getName(self):
        return self.name

    def touch(self, filename):
        self.files.append(filename)
    
    def mkdir(self, directory_name):
        self.directories.append(Directory(directory_name))

    def ls(self):
        for file in self.files:
            print(file, end="  ")
        for directory in self.directories:
            print(directory.name, end="  ")
    



def main():
    root = Directory("bin")
    current_dir = root
    root.touch('main.py') 
    root.touch('fast.py')
    root.mkdir('projectsofmine')
    root.ls()
    print()


main();