
#  Q1
def push(Stack,item):
    if len(Stack) == 5:
        print ('Stack ເຕັມແລ້ວ')
    else:
        Stack.append(item)
        print(f"ເພິ່ມ{item}ເຂົ້າ Stack ສຳເລັດແລ້ວ")
def pop(Stack):
    if len(Stack)==0:
        print('Stack ວ່າງ!')
    else:
        item=Stack.pop()
        print(f"ນຳເອົາ{item} ອອກຈາກ Stackສຳເລັດແລ້ວ")
def display(Stack):
    if len (Stack)==0:
        print('Stack ວ່າງ!')
    else:
        print("Stack ປະກອບມີ: ")
        for item in reversed (Stack):
            print(item)
Stack= []
while True:
    print('\n')
    print('=========================')
    print(' ຈັດການໂຄງການ Stack ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Stack: ')
    print('2.ເອົາຂໍ້ມູນອອກ Stack:')
    print('3.ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Stack: ')
    print('4.ອອກຈາກໂປຣແກຣມ: ')
    print("========================")
    choice = int(input("Enter the choice:"))
    if choice in (1, 2, 3, 4):
        if (choice==4):
            break
        if (choice==1):
              item=int(input('ປ້ອນຂໍ້ມູນລົງໃນ Stack :'))
              push(Stack,item)
        elif (choice==2):
            pop(Stack)
        elif (choice==3):
         display(Stack)
    else:
        print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງn")
       
