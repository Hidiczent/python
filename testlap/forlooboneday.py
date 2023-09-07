# # # # # for i in range (0,5,2 ):
# # # # #     print(i,"I'am sorry her ")
# # # # # for i in range (0,5,1 ):
# # # # #     print(i,end= ' ')
# # # # # print(list(range (0,5, 1)))
# # # # # print(list(range (0,5, 2)))
# # # # # print(list(range (-2,-10, -2))
# # # # # n= int(input("Enter a number :"))
# # # # # fact=1
# # # # # for i in range(1,n+1):
# # # # #     fact = fact *i
# # # # # print(str(fact * i))

# # # # # BTS=['V','J-Hope','RM','Jungkook','Jin','jimmin','Suga']
# # # # # for i in BTS:
# # # # #     print(i)

# # # # # s = 0
# # # # # for i in range  (1,101):
# # # # #     s+=i
# # # # # print(" Sum of number from 1 to 100",s)
# # # # # s=0
# # # # # for i in range  (0,101,2):
# # # # #     s+=i
# # # # # print(" Sum of number from 1 to 100",s)
# # # # n=int(input("Enter number:"))
# # # # num = 1
# # # # k = 1
# # # # for i in range(1, n + 1):
# # # #     for j in range(1, n + 1):
# # # #         print(num,"\t", end = "")
# # # #         num = num + k
# # # #     if i % 2 == 1:
# # # #         num = num + n - 1
# # # #         k = -1
# # # #     else:
# # # #         num = num + n + 1
# # # #         k = 1
# # # #     print("")



# # # # n = int(input ("Enter n :"))
# # # # matrix = [[0]*n for i in range(n)]  #ສ້າງໃຫ້ matrix ມີຂະຫນາດ n*n 2D
# # # # num = 1
# # # # for result in matrix:
# # # #     print(result)
# # # # print("\n")
# # # # for i in range :
# # # #     if i % 2 == 0:
# # # #         for j in range(n):
# # # #             matrix[i][j] = num
# # # #             num+=1
# # # #     else:
# # # #         for j in range(n-1,-1,-1):
# # # #             matrix[i][j] = num
# # # #             num+=1
# # # # for result in matrix:
# # # #     print(result)



i = 1
j=1
while  j <= 9:
    print(i*j)
    j+=1
    
# # ຂໍ້2
# i = 1
# while i <=9:
#     j =1
#     while j < 10:
#         print(i,'x',j,'=',i*j)
#         j += 1
        
#     i += 1






# # # current_pos=0
# # # days=1
# # # move_up=7
# # # move_down=5
# # # destination =30
# # # current_pos +=move_up

# # # print("days:",days,'Snails position ',current_pos,'meters')

# # # while (current_pos <= destination):
# # #     current_pos-=move_down
# # #     days+=1
# # #     current_pos += move_up
# # #     print("days:",days,'Snails position ',current_pos,'meters')
# # # print()
# # # print('it took {} day to get out of the will',format(days))


# # # for i in range(5):
# # #     print("hi hi hi ")



# # n=int(input("Enter number to sum p to"))
# # s=0
# # i=1

# # while i<=n:
# #     s = s+i
# #     i+=1
# #     print('Sum of 1 to {} is {}'.format(n,s))

# selected=None
# while selected not in ['scissors ','Rock','paper : ']:
#     selected = input('Chose amog scissors , Rock, paper')
# print("chose value: ", selected )

# n=-1
# while n<=0:
#     n=int(input("Enter a positive nmber to sum up to "))
# s=0
# for i in range(1,n+1):
#     s=s + 1
# print("Sum of 1 to {} is {} ".format(n,s))
# import random as rd
# numlist=[10,20,30,40,50]
# # rd.shuffle(numlist)
# # print(numlist)
# print(rd.choice(numlist))
# print(rd.sample(numlist,5)) #ເອິ້ນຂໍ້ມູນອອກມາໃຊ້ແລະຕ້ອງລະບຸູຈຳນວນ

# st = 'Programming'
# for ch in st:
#     if ch in ['a','e',"i",'o','u']:
#         # break
#         continue
#     print(ch)
# print( "The end ")

# for i in range (2,10):
#     for j in range(1,10):
#         print('{}x{}={:2d}, '.format(i,j,i*j),end='')
#     print()

import random as rd
secre_number = rd.randint(1,100)
