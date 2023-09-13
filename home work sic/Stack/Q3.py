from queue import LifoQueue
import time
LIFO= LifoQueue()
while True: 
    print('\n')
    print('=========================')
    print(' ຈັດການໂຄງການ Stack ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Stack: ')
    print('2. ເອົາຂໍ້ມູນອອກ Stack:')
    print('3. ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Stack: ')
    print('4. ອອກຈາກໂປຣແກຣມ: ')
    Data=int(input('ເລືອກສິ່ງທີ່ເຈົ້າຕ້ອງການ: '))
    if Data in (1,2,3,4):
        if (Data == 4):
             break
        if (Data == 1):
            if (LifoQueue(maxsize=5)):
                print('Stack ເຕັມແລ້ວ ')
            else : 
                d=int(input('ໃສ່ Stack: '))
                LIFO.put(d)
                time.sleep(1)
        elif ( LIFO ==2 ):
             if len(LIFO==0):
                 print('Stack ວ່າງ! ')
             else :
                 print(' ເອົາຂໍ້ມູນອອກຈາກ Stack ',LIFO.get())
                 time.sleep(1)
        elif (LIFO == 3):
                print('Stack = ', LIFO)
                time.sleep(1)
        else:
             print('ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງ')