# import string
# def cipher(a):
#     idx = src_str.index(a)
#     return dst_str[idx]
# src_str=string.ascii_uppercase
# dst_str= src_str[3:]+ src_str[:3]

# src=input('Enter a sentence: ')
# print('Encrypted text : ',end='')

# for ch in src:
#     if ch in src_str:
#         print(cipher(ch),end='')
#     else:
#         print(ch,end='')
# print()

# def printstar(): ແບບບໍ່ຮັບຄ່າແລະບໍ່ສົ່ງຄ່າ 
#     print('*******************')
# for _ in range(2):
#     printstar()

# def get_sum(start,end):#ແບບຮັບຄ່າ ແລະ ສົ່ງຄ່າ
#     s = 0
#     for i in range(start,end+1):
#         s+=i
#     return s 

# x = get_sum(1, 10)
# print(x)
# def print_satar2(n): #ແບບຮັບຄ່າແຕ່ບໍ່ສົ່ງຄ່າອອກ
#     for i in range(n):
#         print('***************')
# print_satar2(10)

# def print_hello(n):
#     print('Hello '*n)
# print_hello(5)

# def ged_sum(a,b):
#     result=a+b
#     print('The sum of', a, 'and', b, 'is',result)
# ged_sum(10,20)
# ged_sum(100,200)

# def square_area(a,b):
#     result=a * b
#     return result

# square_area(100,5)

# def greet(*name):# ແມ່ນການກຳນົດຄ່າຕາມໃຈ
#     for name in name:    
#         print('Hello ',name)
# greet('Liza')
# greet('Are you well ?')

# def sum_num(*numbers): #
#     result = 0
#     for n in numbers:
#         result +=n
#     return result

# print(sum_num(10,20,60,100))
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# for celsius in range(10, 51, 10):
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     print(f"{celsius} Celsius = {fahrenheit} degrees Fahrenheit")

# # Q3
# def mile_to(miles):
#     kilometers = miles * 1.60934
#     return kilometers
# for miles in range(1, 6):
#     kilometers = mile_to(miles)
#     print(f"{miles} mile = {kilometers:.2f} kilometers")
# #   print('The greater of ',m,'or','')

# def max(m,n):
#     if m>n:
        
#         return  m
#     else:
#         return n
# def min(m,n):
#     if m<n:
#         return m
#     else:
#         return n
# print('The greater of 100, or ,200, is:',max(100,200))
# print('The smaller of 100 or 200 is',min(100,200))

# def welcome():
#     print('Welcome.')
# welcome()
# welcome()
def mean3(a,b,c):
    avg=(a+b+c)/3
    return avg
def max3(a,b,c):
    return max(a,b,c)
def min3(a,b,c):
    return min(a,b,c)
a,b,c=(input('Enter three number ')).split()
a=int(a)
b=int(b)
c=int(c)
print('The average value of ',a,b,c ,mean3(a,b,c))
print('The maximum value of ',a,b,c,max3(a,b,c))
print('The minimum value of ',a,b,c,min3(a,b,c))
# def min3(a,b,c):