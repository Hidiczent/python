# person1=['David',20,1,180.0,100.0]
# person2=['john smith',25,1,170.0,70.0]
# person3=['jane carter ',22,0,169.0,60.00]
# person4=['peter kelly',40,1,150,50.0]
# person_list= person1+person2+person3+person4

# n_person= int(len(person_list)/5)
# age_sum=0.0
# for age in person_list[1::5]:
#     age_sum+=age
# aveage_age= float(age_sum) / n_person
# print("The  average age is "+str(aveage_age))
# prime_list=[2,3,5,7]
# # print(n_list)

# prime_list.append(11)
# print('Prime number After addition',prime_list)

# list1=[3,5,7]
# list2=[2,3,4,5,6]
# for i in list1:
#     for j in list2:
#         print(i,'x',j,"=",i*j)

# s_list=['abc','bcd','bcdfg','abba','cddc','opq']
# a=s_list[0]
# for i in s_list:
#     if len(a)==len(i):
#         a=i
#         print(a,end=" ")

# s_list=['abc','bcd','bcdfg','abba','cddc','opq']
# for i in s_list:
#     if len(s_list)>len(i):
#         print(s_list,end=" ")

# s_list=['abc','bcd','bcdfg','abba','cddc','opq']
# a=s_list[0]
# for i in s_list:
#     if len(i) < len(a):
#         a=i
# print(a)

# menu={'Americano':3000,'Ice  Americano':3500,'Cappucino':4000,'Cafe latte':4500,'Epresso':3600}
# for key in menu:
#     print('{:16s} price : {:,} KRM'.format(key,menu[key]))
# choice=input("select one menu from the lsit: ")
# if choice in menu.keys():
#     print('{} is {:,} KRM, Pease make a payment: '.format(choice,menu[choice]))
# else:
#     print('Sorry {} is not in the menu'.format(choice))
# paper coding 
# 1
# capital_dic={'Korea':'Seoul','Chaina':'Beijing','USA':'Washigton DC'}
# print(capital_dic['Korea'])

# fruis_dic={'Apple':5000,'banana':4000,'grape':5800,'Melon':6500}
# for key in fruis_dic:
#     print('The price of an {} is {} KRM.'.format(key,fruis_dic[key]))

# import json
# data='{"title":"The old man and the sea","ISBN":"12345","Author":"Ernest HEminfway"}'
# json_data=json.loads(data)
# print(type(json_data))
# print(json_data)
# print(json_data['ISBN'])

# fruits_dic={'apple':6000,'Melon':3000,'banana':5000,'orange':4000}
# dict_key=list(fruits_dic.keys())
# print(dict_key)
# l=['apple','melon']
# for item in l:
#     if 'apple' in  fruits_dic:
#         print(item,' is in fruis_dic')
#     else:
#         print(item,'is not fruits_dic')

# population_a=(100,150,230,120,180,100,140,95,81,21,4)
# population_b=(300,420,530,420,400,300,40,5,1,1,1)
# oldA=sum(population_a[7:])
# oldB=sum(population_b[7:])
# sumA,SumB= sum(population_a),sum(population_b)
# oldRateA,oldRateB=oldA/sumA,oldB/SumB
# print('the degrees of aging in town A and B  are {:5.3f} and {:5.3f} respectively.'.format(oldRateA,oldRateB)) 
# num_tuple = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)
# max_count = 0
# most_freq_num = None
# for num in num_tuple:
#     count = num_tuple.count(num)
#     if count > max_count:
#         most_freq_num = num
#     elif count == max_count and num > most_freq_num:
#         most_freq_num = num
#     else:
#         pass
# print("The most frequent element:", most_freq_num)

# matrix =  [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for row in range(4):
#     for element in matrix[row]:
#         print(element,end=' ')
#     print()
# import random
# seat =[]
# for i in range (3):
#     line=[]
#     for j in range(6):
#         rand=random.randrange(0,2)
#         line.append(rand)
#     seat.append(line)
# avilable=0
# for i in range(3):
#     for j in range(6):
#         print(seat[i][j], ' ',end=' ')
#         if seat[i][j]==0:
#             avilable+=1
#     print()
# print('The number of remaining seats in the theater: ',avilable)



# n_values = input("Enter n values separated by spaces: ")
# n_list = n_values.split()
# n = len(n_list)
# matrix = []
# for i in range(int(n_list[0])):
#     row = []
#     for j in range(int(n_list[0])):
#         row.append((i+j) % 2)
#     matrix.append(row)
# for k in range(1, n):
#     for i in range(int(n_list[k])):
#         for j in range(int(n_list[0])):
#             matrix[i][j+k*int(n_list[0])] = (i+j) % 2
# for row in matrix:
#     for element in row:
#         print(element, end='')
#     print()
# n = int(input("Enter n: "))
# for i in range(n):
#     for j in range(n):
#         if (i+j) % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()
# array=[[10,20], # Q1
#        [30,40],
#        [50,60]]
# print(array[1][0])




# n = int(input("Enter n: "))
# arr = [[0 for j in range(n)] for i in range(n)]
# print(arr)
# for i in range(n):
#     for j in range(n):
#         if (i + j) % 2 == 0:
#             arr[i][j] = 1
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end=' ')
#     print()

# list_array=[i for i in range(10) if i % 2 == 0]


# persion={'LastName':'Doe','FirstName':'David','Company':'Sanmsung'}
# for i in persion:
#     print('{} : {}'.format(i,persion[i]))

# str1= ['a','b','c','b','a','b','c']3

# dic={}
# for ch in str1: 
#     if ch not in dic.keys():
#         dic[ch] = 0
#     dic[ch] += 1
# print('Alpabet counting:',dic)

# dic={'a':10,'b':20,'c':30,'d':40}
# dic.setdefault('f',50)
# print(dic)
# dic2={}
# dic2.setdefault('w',10)
# print(dic2)
# dic2.update(w=100)
# print(dic2)


# persion={'LastName':'Doe','FirstName':'David','Company':'Sanmsung'}
# for i in persion:
#     print('{} : {}'.format(i,persion[i]))

# items = {"Coffee": 7,"Pen": 3,"Paper cup": 2,"Milk": 1,"Coke": 4,"Book": 5}
# item_name = input("Enter the name of the item: ")
# if item_name in items:
#     print(items[item_name])
# else:
#     print("Item not found in inventory.")


# choie=str(input('Selectmenu 1)Checkstock 2) Warehosing3) release 4) exit: '))
# items = {"Coffee": 7,"Pen": 3,"Paper cup": 2,"Milk": 1,"Coke": 4,"Book": 5}
# item_name ={}
# if choie == '2':
#     if item_name in items:
#         item_name = input("Enter the name of the item: ")
#         print(items[item_name])
# tele_dic_dic={'Chinese restaurant':('101-1234-4500'),'japanese retaurant':('101-2230-6540'),'Italian':('010-3232-7788')}
# print('Previos number')

# for key,value in tele_dic_dic.items():
#     print(key+':'+value)
# for key,value in tele_dic_dic.items():
#     adr,review=input(key+'Please write address and review of: ').split()
#     update=(value,adr,review)
#     tele_dic_dic[key]=update
# print('Update number')
# for key,value in tele_dic_dic.items():
#     print(key + ':',value)

#ເພິ່ມຈຳນວນໃຫ້ກັບdic
# from collections import defaultdict
# word='acbaabca'
# counter =defaultdict(int)
# for letter in word:
#     counter[letter] +=1
# print(counter)
# terrestrial_planet = {   #doubledictionary
# 'Mercury': {
# 'mean_radius': 2439.7, 
# 'mass': 3.3022E+23,
# 'orbital period': 87.969
# }, 
# "Venus": {
# 'mean_radius': 6051.8, 
# 'mass': 4.8676E+24,
# 'orbital period': 224.70069,
# },
# 'Earth': {
# 'mean_radius': 6371.0,
# 'mass': 5.97219E+24,
# 'orbital period': 365.25641,
#  },
# 'Mars': {
# 'mean_radius': 3389.5,
# 'mass': 6.4185E+23, 
# 'orbital period': 686.9600,
# }
#  }
# print(terrestrial_planet['Venus']['mean_radius'])
# import copy
# x={'a':{'python':'2.7'},'b':{'pyhon':'3.6'}}
# y=copy.deepcopy()
# y['a']['python']='5.0'
# print(x)
# y is x


# study_tup = (('211101', 'David Doe', '010-1234-4500'), ('211102', 'John Smith', '010-2230-6540'), ('211103', 'Jane Carter', '010-3232-7788'))
# for tup in study_tup:
#     study_dict = {tup[0]: [tup[1], tup[2]]}
#     print(study_dict)
# inp = input("Enter student ID: ")
# for tup in study_tup:
#     if inp == tup[0]:
#         print("Name:", tup[1])
#         print("Phone number:", tup[2])
#         break
# else:
#     print("not student ID")

study_tup = [('211101', 'David Doe', '010-1234-4500'), ('211102', 'John Smith', '010-2230-6540'), ('211103', 'Jane Carter', '010-3232-7788')]
student_dict={}


for student in study_tup:
    student_id, student_name, phone_number = student
    print(student_id, ':',student_name)
    student_dict[student_id] = student_name

student_id =input("Enter student ID number: ")

if student_id in student_dict:
    for student in study_tup:
        if student[0] == student_id:
            print(student[0],"student is ", student[1],'and phone number is',student[2],'.')
            break
else:
    print("Student ID not found.")