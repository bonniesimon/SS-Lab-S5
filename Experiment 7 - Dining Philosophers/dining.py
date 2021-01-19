def all_philosophers_comp(phils,p):
    for i in range (p) :
        if (phils[i]!=1):
            return 0
    return 1;

p=int(input("Enter the Number of Philosophers : "))
chops = [0]*p
philosophers_comp = [0]*p
flag = 1
for i in range (p) :
        chops[i]=1       
while (flag):
        for i in range (p) :
              chops[i]=1       
        flag = 0
        for i in range (p) :
        
            if (philosophers_comp[i]!=1):
                if (chops[i] and chops[(i + 1) % p]):
                    chops[i] = 0
                    chops[(i + 1) % p] = 0
                    print("\nPhilosopher ",i," is Eating.")
                    philosophers_comp[i] = 1
                    flag = 1
                
                else:
                    print("\nPhilosopher ",i," is Thinking.")
            
            else:
                print("\nPhilosopher ",i," has Finished Eating.")

        if (all_philosophers_comp(philosophers_comp, p)):
            print("\nProgram Completed Successfully.")
            exit(0)
            
print("\nDeadlock is Present!!")