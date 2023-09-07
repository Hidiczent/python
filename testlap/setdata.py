# cases_3time=set()
# for i in range(1,7):
#     for j in range(1,7):
#         for k in range(1,7):
#             cases_3time.add((i,j,k))
# total_cases=len(cases_3time)
# print("Event that can happen by rolling the dice 3 times are ",total_cases,'cases')
# for  a in range(3,19):
#     total_cases=0
#     n_cases=0
#     for c in cases_3time:
#         if  sum(c) >=a:
#             n_cases+=1
#     prop=n_cases*100/total_cases
#     print('probability of getting more than {:2d}is {:6.2f}%'.format(a,prop))

# day_list=['Mon','tue','Wed','Thu','Fri','Sat','Sun']
# day_set=set(day_list)
# print(day_set)
# fruist_tuple=('Apple','Orange','Water Melon')
# fruist_set=set(fruist_tuple)
# print(fruist_set)
# h_str='hello'
# h_set=set(h_str)
# print(h_set)
# number={2,3,4}
# number.add(1)
# print(number)
# number.remove(4)
# print(number)
# number.discard(2)
# print(number)

# l1=[1,2,3,1,2]
# print(set(l1))
# s2=set(l1)
# print(sorted(s2))
# s1='avcdefa'
# print(set(s1))
# s1={1,2,3,4,5,6}
# s2={4,5,6,7,8,9 }
# print(s1&s2)
# print(s1.intersection(s2))
# s1={10, 20, 30, 40}
# s2={30, 40, 50, 60,70}
# print(s1 | s2) 
# print(s1 & s2)
# print(s1 - s2) 
# print(s1 ^ s2) 
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s1.isdisjoint(s2))
# A={1,3}
# B={2,4}
# res=set()
# for i in A:
#     for j in B:
#         res=res|{(i,j)}
# AxB=res
# print("A = ",A)
# print("B = ",B)
# print("AxB = ",AxB)

# lst=['Apple','Mango','banana']
# s1=set(lst)
# print(s1)
# a_set={1,0,2,3,3}
# all(a_set)

# mylist=[(1,2),(4,5),(4,2),(3,1),(9,4)]
# lst=int('Enter two integers').split()
# for i in mylist:
#     if mylist 
# while True:
#     a, b = map(int, input("Enter two integers: ").split())
#     found = False
#     for i, (m, n) in enumerate(mylist):
#         if (a, b) == (m, n):
#             print(f"There is ({a},{b}) at the {i+1}st.")
#             found = True
#             break
#         elif (b, a) == (m, n):
#             print(f"There is no ({a},{b}) but there is ({b},{a}) at the {i+1}st.")
#             found = True
#             break
#     if not found:
#         print(f"There is no ({a},{b}) nor ({b},{a})")

# mylist = [(1, 2), (4, 5), (3, 4)]
# while True:
#     s = input("Enter two integers: ")
#     a = int(s.split()[0])
#     b = int(s.split()[1])
#     found = False
#     for i, (m, n) in enumerate(mylist):
#         if (a, b) == (m, n):
#             print(f"There is ({a},{b}) at the {i+1}st.")
#             found = True
#             break
#         elif (b, a) == (m, n):
#             print(f"There is no ({a},{b}) but there is ({b},{a}) at the {i+1}st.")
#             found = True
#             break
#     if not found:
#         print(f"There is no ({a},{b}) nor ({b},{a})")
# mylist = [(1, 2), (4, 5), (3, 4)]

# mylist = [(1, 2), (4, 5), (3, 4)]
mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]
while True:
    s = input("Enter two integers: ")
    split_s = s.split()
    a = int(split_s[0])
    b = int(split_s[1])
    found = False
    for i in range(len(mylist)):
        if (a, b) == mylist[i]:
            print(f"There is ({a},{b}) at position {i}.")
            found = True
            break
        elif (b, a) == mylist[i]:
            print(f"There is ({b},{a}) at position {i}.")
            found = True
            break
    if not found:
        print("There is not in mylist.")
