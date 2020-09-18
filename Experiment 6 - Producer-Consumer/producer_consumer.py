from termcolor import colored


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
    buffer = [0 for i in range(n)]
    print("type 'help' for command")
    while(True):
        print(colored(">> ","blue"), end=" ")
        user_input = input()
        command = user_input.split()[0]
        try:
            data = int(user_input.split()[1])
        except:
            pass
        if(command == "produce"):
            if(i < n-1):
                i += 1
                buffer[i] = data
                print_buffer(buffer)
            else:
                print("Buffer Full!")
        elif(command == "consume"):
            if(i >= 0):
                print("Data consumed is ", buffer[i])
                buffer[i] = 0
                i -= 1
                print_buffer(buffer)
            else:
                print("Buffer is empty!")
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