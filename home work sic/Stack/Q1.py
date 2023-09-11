
#  Q1
from collections import deque
import time
Stack= []
while True:
    print("\n")
    print("========================")
    print("Manage Stack Program")
    print("1. Push data")
    print("2. Pop data")
    print("3. Display the value of Stack Program")
    print("4. Exit the program")
    print("========================")
    c = int(input("Enter the choice:"))

    if c in (1, 2, 3, 4):
        if (c==4):
            break
        #first check whether user want to exit
        # Singly Linked List with insertion, finding and print methods
        if (c==1):
              if len(Stack)==5:
                print("The Stack  is full!")
              else :
                  d=int(input('Enter the Stack'))
                  Stack.append(d)
                  time.sleep(0.01)
        elif (c==2):
             if len(Stack)==0:
                print("The Stack is is full!")
             else :
                print("Pop element is",Stack.pop())
                time.sleep(0.01)
        elif (c==3):
            print("Stack =",Stack)
            time.sleep(0.01)
    else:
        print("Invalid Choice, please try again")
        time.sleep(0.01)
