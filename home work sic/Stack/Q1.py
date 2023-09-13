
#  Q1
from collections import deque
import time
Stack= []
while True:
    print('\n')
    print('=========================')
    print(' ຈັດການໂຄງການ Stack ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Stack: ')
    print('2. ເອົາຂໍ້ມູນອອກ Stack:')
    print('3. ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Stack: ')
    print('4. ອອກຈາກໂປຣແກຣມ: ')
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
