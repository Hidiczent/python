# # def valid_date(date):
# #     days=[31,29,31,30,31,30,31,30,31,30,31,30,31]
# #     sherlock_series=[1887,1890,1892,1894,1901,1905,1915,1917,1927]
# #     splitted=date.split('.')
# #     year=int(splitted[0])
# #     month=int(splitted[1])
# #     days=int(splitted[2])
# #     is_sherLock_book_yr=lambda x:x in sherlock_series
# #     if not is_sherLock_book_yr(year):
# #         print('This is not a publication year to the Sherlock Holmes series.')
# #         return False
# #     if month < 1 or month >12:
# #         print('The month is incorrect.')
# #         return False
# #     if days < 1 or days >days[month-1]:
# #         print('the data is incorrect.')
# #         return False
    
# #     return False 
# # date=input('Distingquish year ,month ad date by.(e.g.1917.6.10): ')
# # if valid_date(date) ==True:
# #     print('This is the  a publication year to the Sherlock Holmes series.')
# # else:
# #     print('This  not a the publication dae of a sherlock holmes series or the input has an error')

# # add=lambda x,y:x+y
# # print('Sum of 100 and 200: ',add(200,100))
# # a =[1,2,3,4,5,6,7]
# # square_a=list (map(lambda x:x**2,a))
# # print(square_a)

# # def adult_func(n):
# #     if n>=19:
# #         return True
# #     else:
# #         return False
# # ages=[34,39,20,18,13,54]
# # for a in filter(adult_func,ages):
# #     print(a,end=' ')

# # a=[1,2,3,4,5,6,7]
# # square_a=[]
# # for n in a :
# #     square_a.append(n**2)
# # print(square_a)
# # def square(x):
# #     return x**2
# # a=[1,2,3,4,5,6,7]
# # square_a=list(map(square_a))
# # def square(x):
# #     return x**2
# # a=[1,2,3,4,5,6,7]
# # square_a=list(map(square , a))
# # print(square_a)

# # a=[1,2,3,4,5,6,7]
# # cubic_a=list(map(lambda x:x**3,a))
# # print(cubic_a)
# # Q1
# # n_list=[1,2,3,4,5,6,7,8,9,10]
# # even_list=[]
# # for i in filter(lambda x :x%2==0,n_list):
# #     even_list.append(i)
# # print(even_list)

# # n_list=[1,2,3,4,5,6,7,8,9,10]
# # even_list=list(filter(lambda x:x%2==0,n_list))
# # print(even_list)

# # def to_upper(x):
# #     return x.upper()
# # a_list=['a','b','c','d']
# # square=list(map(to_upper,a_list))
# # print(square)

# # from functools import reduce
# # num=range(1,101)
# # sum_1=reduce(lambda x,y:x+y,num)
# # print(sum_1)

# scores=[100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]
# num_students = len(scores) // 3
# valid_scores = list(filter(lambda x: 0 not in x, zip(scores[::3], scores[1::3], scores[2::3])))
# num_valid = len(valid_scores)
# valid_only = [x for x in zip(scores[::3], scores[1::3], scores[2::3]) if 0 not in x]
# print("Number of students' scores:", num_students)
# print("Number of students with valid scores for all subjects:", num_valid)
# print("Scores of students with only valid scores:", valid_only)