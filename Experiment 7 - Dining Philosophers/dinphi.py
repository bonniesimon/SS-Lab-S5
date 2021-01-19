n=int(input("Enter the number of philosophers: "))
st=[0]*n 
while(1): 
    p = int(input("Enter the philosopher index :")) 
    ch=int(input("1. Pickup the chopstick\n2. Put down the chopstick\nChoose: ")) 
    if(ch==1): 
         st[p]=1 
         print("Philosopher "+str(p)+" is hungry.") 
         if(st[(p+(n-1))%n]!=2 and st[p]==1 and st[(p+1)%n]!=2): 
             st[p]=2 
             print("Philosopher "+str(p)+" is eating.") 
         else:
            print("Philosopher "+str(p)+" cannot eat.")
    else: 
        st[p]=0
        print("Philosopher "+str(p)+" is thinking.") 
        a=(p+(n-1))%n 
        b=(p+1)%n 
        if(st[(a+(n-1))%n]!=2 and st[a]==1 and st[(a+1)%n]!=2):
            st[a]=2 
            print("Philosopher "+str(a)+" is eating.") 
        else: 
            print("Philosopher "+str(a)+" cannot eat.")
        if(st[(b+(n-1))%n]!=2 and st[b]==1 and st[(b+1)%n]!=2): 
            st[b]=2
            print("Philosopher "+str(b)+" is eating.") 
        else: 
            print("Philosopher "+str(b)+" cannot eat.")