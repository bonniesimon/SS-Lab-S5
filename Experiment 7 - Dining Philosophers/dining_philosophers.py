
def clear_chopsticks(chopstick):
    for item in chopstick:
        item = True
    return

def all_philosophers_finished_eating(philosopher_finished_eating):
    for item in philosopher_finished_eating:
        if(not item):
            return False
    return True

def main():
    n = 9
    philosopher_finished_eating = [ 0 for i in range(n)]
    chopstick = [1 for i in range(n)]
    flag = True

    while(flag):
        print("---------------------------------Next Pass---------------------------------")
        clear_chopsticks(chopstick)
        flag = False

        for i in range(n):
            if(not philosopher_finished_eating[i]):
                if(chopstick[i] and chopstick[(i+1)%n]):
                    chopstick[i] = False
                    chopstick[(i+1)%n] = False
                    print(f"Philosopher {i} is eating")
                    philosopher_finished_eating[i] = True
                    flag = True
                else:
                    print(f"philosopher {i} is thinking")
            else:
                print(f"Philosopher {i} has finished eating")
        if(all_philosophers_finished_eating(philosopher_finished_eating)):
            print("All philosophers eat successfully!")
            exit()
    print("Deadlock present!")

main()