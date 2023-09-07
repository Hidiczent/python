# l1=['1 like','I love']
# l2=['pancake','kiwi juice','esprsso']
# for i in l1:
#     for j in l2:
#         print(i,j)

# person={'Name':'David Doe','Age':'26','weight':'78','Job':'Data Sicentist'}
# person2={'father':'jhon Doe'}
# person.update(person2)
# print(person)

# maria = {'Korean':94,'Englisht':91,'Mathematics':89,'Scicene':83}
# const =len(maria)
# scr = maria.values()
# score =sum(scr)
# arg = score/const
# print("Average: ",arg)

# # Arr1=[[1,2],[3,4],[5,6]]
# Arr2=[]
# for i in Arr1:
#     Arr2.extend(i)
# print(Arr2)
# import copy
# school={'kim':{'age':16,'hie':170,"grade" : 3},
#         'lee':{'age':15,'hei':168,"grade":2},
#         'Choi':{'age':14,'hie':173,"grade" :1},
#         }
# school2=copy.deepcopy(school)
# print(school is school2)
score=(('dongkyu Prak',88,95,90),('youngMin Kang',85,90,95),('DongMinPrak',70,90,80),('seungJoo Hong',90,90,95))
s1,s2,s3,s4=zip(*score) 
s_um=sum(s3)
arg=s_um/4
print(arg)