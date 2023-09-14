
Stack={}
while True:
    print('\n')
    print('=========================')
    print(' ຈັດການໂຄງການ Stack ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Stack: ')
    print('2. ເອົາຂໍ້ມູນອອກ Stack:')
    print('3. ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Stack: ')
    print('4.ກວດສອບ Stack ວ່າເຕັມຫຼືບໍ່: ')
    print('5.Clear stack')
    print('6.ອອກຈາກໂປຣແກຣມ')
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
                    key = input('Enter key: ')
                    value = input('Enter value: ')
                    Stack[key] = value
        elif (c==2):
            if not Stack:
                print("Stack ว่าง!")
            else:
                key = input("Enter key to delete: ")
            if key in Stack:
                del Stack[key]
                print("Deleted key:", key)
            else:
                print("Key not found!")
    
        elif (c==3):
            print("Stack =",Stack)
    else:
        print("Invalid Choice, please try again")