
from queue import LifoQueue
LIFO= LifoQueue(maxsize=5)
while True: 
    print('\n')
    print('=========================')
    print(' ຈັດການໂຄງການ Stack ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Stack: ')
    print('2. ເອົາຂໍ້ມູນອອກ Stack:')
    print('3. ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Stack: ')
    print('4. ອອກຈາກໂປຣແກຣມ: ')
    Data=int(input("ເລືອກສິ່ງທີ່ເຈົ້າຕ້ອງການ: "))
    if Data in (1,2,3,4):
        if (Data == 4):
             break
        if (Data == 1):
            if LIFO.full():
                print('Stack ເຕັມແລ້ວ!')
            else : 
                key=input('ໃສ່ key')
                value=input('ໃສ່ velue')
                d=int(input('ໃສ່ Stack: '))
                LIFO.put({key:value})
             
        elif (Data == 2):
             if LIFO.empty():
                 print(' Stack ວ່າງ!')
             else :
                 print("ນຳຂໍ້ມູນອອກຈາກ Stack ",LIFO.get())
                 
        elif (Data == 3):
                print('Stack = ', list(LIFO.queue))
                
        else:
             print('ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງ')
             