class Queue:
    def __init__(self):
        self.items = {}
    def push(self,key,value):
        if not  self.is_full():
            print(f" ເພິ່ມ key {key} ເຂົ້າ Queue ສຳເລັດແລ້ວ")
            self.items[key]=value
        else:
            print('Queue ເຕັມແລ້ວ ')
    def pop (self,key):
        if not self.is_empty():
            if key in self.items:
                value = self.items.pop(key)
                print(f"ນຳເອົາkey {key} ອອກຈາກ Queueສຳເລັດແລ້ວ")
                return value
            else:
                print('ບໍ່ພົບ key')
        else:
            print('Queue ວ່າງ')

    def is_full(self):
        return len(self.items)==10
    
    def is_empty(self):
        return not self.items
    
    def clear(self):
        self.items.clear()
    

queue=Queue()

while True:
    print('\n')
    print('=========================')
    print(' ຈັດການໂຄງການ Queue ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Queue: ')
    print('2. ເອົາຂໍ້ມູນອອກ Queue:')
    print('3. ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Queue: ')
    print('4.ກວດສອບ Queue ວ່າເຕັມຫຼືບໍ່: ')
    print('5.Clear queue')
    print('6.ອອກຈາກໂປຣແກຣມ')
    print("========================")

    choice =int(input('ເລືອກສິ່ງທີ່ຕ້ອງການ: '))

    if choice in (1,2,3,4,5,6):
        if (choice==1):
            key=input('ປ້ອນkey: ')
            value=input('ປ້ອນvalue: ')
            queue.push(key,value)
        elif (choice==2):
            key=input('ນຳເອົາkeyອອກ: ')
            queue.pop(key)
        elif (choice == 3):
            print('Queue ',queue.items)
        elif (choice == 4 ):
            if queue.is_full():
                print('Queue ເຕັມແລ້ວ')
            else:
                print('queueຍັງບໍເຕັມ')
        elif (choice ==5 ):
            queue.clear()
            print('Queue cleared.')
        
        elif (choice == 6):
            break
    else:
        print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງn")
