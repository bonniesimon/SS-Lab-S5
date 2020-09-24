from termcolor import colored


class CircularQueue(): 
  
    # constructor 
    def __init__(self, size): # initializing the class 
        self.size = size 
          
        # initializing queue with none 
        self.queue = [None for i in range(size)]  
        self.front = self.rear = -1
  
    def enqueue(self, data): 
          
        # condition if queue is full 
        if ((self.rear + 1) % self.size == self.front):  
            print(" Queue is Full\n") 
              
        # condition for empty queue 
        elif (self.front == -1):  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data 
        else: 
              
            # next position of rear 
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = data 
              
    def dequeue(self): 
        if (self.front == -1): # codition for empty queue 
            print ("Queue is Empty\n") 
              
        # condition for only one element 
        elif (self.front == self.rear):  
            temp=self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp 
  
    def display(self): 
      
        # condition for empty queue 
        if(self.front == -1):  
            print ("Buffer is Empty") 
  
        elif (self.rear >= self.front): 
            print("Buffer:",  
                                              end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        else: 
            print ("Buffer:",  
                                           end = " ") 
            for i in range(self.front, self.size): 
                print(self.queue[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        if ((self.rear + 1) % self.size == self.front): 
            print("Buffer is Full") 


def print_buffer(buffer):
    print("Buffer = ", end="")
    for item in buffer:
        if(item == 0):
            print("-", end="  ")
            continue
        print(item, end="  ")
    print()

def main():
    i=-1;
    n = int(input("Enter the buffer size : "))
    # buffer = [0 for i in range(n)]
    buffer = CircularQueue(n)
    head = -1
    tail = -1
    print("type 'help' for command")
    while(True):
        print(colored(">> ","blue"), end=" ")
        user_input = input()
        command = user_input.split()[0]
        try:
            data = int(user_input.split()[1])
        except:
            pass
        if(command == "p"):
            buffer.enqueue(data)
            buffer.display()
        elif(command == "c"):
            buffer.dequeue()
            buffer.display()
        elif(command == 'help'):
            print()
            print("%-22s %-20s" % ("produce <data>", "produces <data> into buffer"))
            print("%-22s %-20s" % ("consume", "produces <data> into buffer"))
            print()
        elif(command == "exit"):
            exit()
        else:
            print("Enter valid command!!")


main()