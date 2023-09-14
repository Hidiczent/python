from queue import Queue
class CustomQueue:
    def __init__(self):
        self.items=Queue(maxsize=10)
    def push(self,item):
        if not self.is_full():
            print(f" ເພິ່ມ {item} ເຂົ້າ queue ສຳເລັດແລ້ວ")
            self.items.append(item)
        else:
            print('queue ເຕັມແລ້ວ! ')
    def pop(self):
        if not self.is_empty():
            print(f" ນຳເອົາ {item} ອອກຈາກ queueສຳເລັດແລ້ວ ")
            return self.items.popleft()
        else:
            print('queue ວ່າງ!')

    def is_full(self):
        return self.items.full()
    
    def is_empty(self):
        return self.items.empty()
    
    def clear(self):
        with self.items.mutex:
             self.items.queue.clear()
 
queue = CustomQueue()

while True:
        print('\n')
        print('=========================')
        print(' queue Management Menu ')
        print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ queue: ')
        print('2.ດຶງຂໍ້ມູນອອກ queue:')
        print('3.ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ queue:')
        print('4.ກວດສອບ queue ວ່າເຕັມຫຼືບໍ່: ')
        print('5.Clear queue')
        print('6.ອອກຈາກໂປຣແກຣມ')
        choie=int(input('ເລືອກສິ່ງທີເຈົ້າຕ້ອງການ:'))
        if choie in (1,2,3,4,5,6):
            if choie == 1:
                item=input('ເພິ່ມຂໍ້ມູນເຂົ້າqueue :')
                queue.push(item)
            elif choie == 2:
                  item = queue.pop()
                  if item is not None:
                    print(f"ລຶບ {item} ແລ້ວ")
            elif choie == 3:
                print('queue= ' , list(queue.items.queue))
            elif choie == 4 :
                if queue.is_full():
                     print('queue ເຕັມແລ້ວ')
                else:
                     print('queue ຍັງບໍ່ເຕັມ.')
            elif choie == 5:
                queue.clear()
                print('queue cleared.')
            elif choie == 6:
                break
        else:
            print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງn")