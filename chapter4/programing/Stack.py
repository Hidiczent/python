# def check(expr):
#     opening="[{("
#     closing="]})"
#     stack=[]
#     for char in expr:
#         if char in opening:
#             stack.append(char)
#         elif char in closing:
#             if len(stack)==0:
#                 return False
#             if opening.index(stack.pop())!=closing.index(char):
#                     return False
#     return len(stack)==0

# str=input("Input a string of parentheses: ")
# print("Valid" if check(str) else "Invalid")




# class Stack:
#     def __init__(self):
#         self.stack=[]

#     def is_Empty(self):
#         return True if len(self.stack)==0 else False

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         return None if self.is_Empty() else self.stack.pop()


# stack=Stack()
# stack.push("A")
# stack.push("B")
# print(stack.pop())
# stack.push("C")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 07:11:52 2022
@author: Bouasoth Xayachak
"""
import time
#create a stack List
stackl = []
while True:
    print("\n")
    print("========================")
    print("Manage Stack Program")
    print("1. Push data")
    print("2. Pop data")
    print("3. Display the value of stack")
    print("4. Exit the program")
    print("========================")
    c = int(input("Enter the choice:"))
    if c in (1, 2, 3, 4):
        if (c==4):
            break
        #first check whether user want to exit

        # Singly Linked List with insertion, finding and print methods
        if (c==1):
              if len(stackl)==5:
                print("The stack is is full!")
              else :
                  d=int(input('Enter the stack'))
                  stackl.append(d)
                  time.sleep(3)
        elif (c==2):
             if len(stackl)==0:
                print("The stack is is full!")
             else :
                print("Pop element is",stackl.pop())
                time.sleep(3)
        elif (c==3):
            print("Stack =",stackl)
            time.sleep(3)
    else:
        print("Invalid Choice, please try again")
        time.sleep(3)

#    if _name_ == '__main__':
#        main()
