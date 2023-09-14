from collections import deque

class Queue:
    def __init__(self):
        self.items=deque(maxlen=10)
    def push(self,items):
        if not self.is_full():
            print(f" ເພິ່ມ {item} ເຂົ້າ queue ສຳເລັດແລ້ວ")
            self.items.append(items)
        else:
            ('queue ເຕັມແລ້ວ.')
    def pop(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
           print('queue ວ່າງ')
    def is_full(self):
        return len(self.items) == self.items.maxlen
    def is_empty(self):
        return len(self.items) == 0
    def clear(self):
        self.items.clear()

queue = Queue()

while True: 
        print('\n')
        print('=========================')
        print(' queue Management Menu ')
        print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ queue: ')
        print('2.ດຶງຂໍ້ມູນອອກ queue:')
        print('3.ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ queue:')
        print('4.ກວດສອບ queue ວ່າເຕັມຫຼືບໍ່: ')
        print('5.Clear stack')
        print('6.ອອກຈາກໂປຣແກຣມ')
        data = int(input('Enter your choice: '))
        if data in (1,2,3,4,5,6):
            if data == 1:
                item = input(' ເພິ່ມຂໍ້ມູນເຂົ້າStack ')
                queue.push(item)
            elif data == 2:
                item = queue.pop()
                if item is not None:
                    print(f" ນຳເອົາ {item} ອອກຈາກ queue ສຳເລັດແລ້ວ ")      
            elif data == 3:
                print('queue = ', queue.items)
            elif data == 4:
                if queue.is_full():
                    print('queueເຕັມແລ້ວ')
                else:
                    print('queueຍັງບໍ່ເຕັມ.')
            elif data == 5:
                queue.clear()
                print('queue cleared.')
            elif data == 6:
                break
        else:
             print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງn")

