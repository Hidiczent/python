# from queue import Queue
import time
#create a Queue List
# q = queue.Queue()
Queue= []
while True:
    print("\n")
    print("========================")
    print("Manage Queue Program")
    print("1. Push data")
    print("2. Pop data")
    print("3. Display the value of Queue Program")
    print("4. Exit the program")
    print("========================")
    c = int(input("Enter the choice:"))

    if c in (1, 2, 3, 4):
        if (c==4):
            break
        #first check whether user want to exit
        # Singly Linked List with insertion, finding and print methods
        if (c==1):
              if len(Queue)==5:
                print("The Queue is is full!")
              else :
                  d=int(input('Enter the Queue'))
                  Queue.append(d)
                  time.sleep(0.01)
        elif (c==2):
             if len(Queue)==0:
                print("The Queue is is full!")
             else :
                print("Pop element is",Queue.pop(0))
                time.sleep(0.01)
        elif (c==3):
            print("Stack =",Queue)
            time.sleep(0.01)
    else:
        print("Invalid Choice, please try again")
        time.sleep(0.01)
