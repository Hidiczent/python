# def hanoi(n,from_,to_,via_):
#     if n==1:
#         print('Number {},{} -> {}'.format(n,from_,to_))
#     else:
#         hanoi(n-1,from_,via_,to_)
#         print('Number {},{} -> {}'.format(n,from_,to_))
#         hanoi(n-1,via_,to_,from_)
# hanoi(3,'A','C','B')
# def circle_area_cicrum(radius):
#     area = 3.14 *radius **2
#     cicrum= 2*3.14*radius
#     return area,cicrum
# radius=100
# area,cicrum=circle_area_cicrum(radius)
# print('Area = ',area)
# print('Circum = ',cicrum)
# def fibonacci(n):
#     if n <= 1:
# # A recursive implementation of the Fibonacci function #Termination condition of the Fibonacci function
#         return n
#     else:
#         return(fibonacci(n-1)+ fibonacci(n-2)) #F_n=F_(n-1) +F_(n-2)
# nterms = int(input("How many Fibonacci numbers do you want: "))
# #Cannot find Fibonacci number if it is negative
# if nterms <= 0:
#     print("Error: Enter a positive number.")
# else:
#   print("Fibonacci sequence: ", end= ' ')
# for i in range(nterms): print (fibonacci(i), end=' ')

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return(fibonacci(n-1)+ fibonacci (n-2)) 
# nterms = int(input("How many Fibonacci numbers do you want?"))
# if nterms <= 0:
#     print("Error: Enter a positive number.")
# else:
#     print("Fibonacci sequence: ", end=' ' )
# for i in range(nterms): print (fibonacci(i), end='')


# def sum_(n):
#     if n <= 1:
#         return 1
#     else:
#         return n + sum_(n-1)
# n=int(input('Enter number:'))
# print('{}!={} '.format(n,sum_(n)))

def power_(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power_(x, y//2) * power_(x, y//2)
    else:
        return x * power_(x, y-1)
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(power_(x, y))


def factorial(k):
    if k == 0:
        return 1
    else:
        return k * factorial(k-1)
def euler(n):
    if n == 0:
        return 1
    else:
        return euler(n-1) + 1/factorial(n)
print("eular(20)={:.5f}".format(euler(20)))
'''
1. เรากำหนดฟังก์ชันที่เรียกว่า `แฟคทอเรียล` ซึ่งรับจำนวนเต็ม `k` และส่งกลับแฟกทอเรียลของ `k` ฟังก์ชันใช้การเรียกซ้ำเพื่อคำนวณแฟกทอเรียล
2. เรากำหนดฟังก์ชันที่เรียกว่า `euler` ซึ่งรับจำนวนเต็ม `n` และส่งกลับผลรวมของอนุกรมเป็น `n` ฟังก์ชันใช้การเรียกซ้ำเพื่อคำนวณผลรวมของอนุกรม
3. ในฟังก์ชัน `euler` เราจะตรวจสอบกรณีฐานโดยที่ `n` เป็น 0 ถ้า `n` เป็น 0 เราจะส่งกลับ 1 เพราะ 1/0! = 1.
4. ถ้า `n` ไม่ใช่ 0 เราจะเรียกฟังก์ชัน `euler` ซ้ำด้วย `n-1` และเพิ่มผลลัพธ์เป็น 1/factorial(n) นี่ทำให้เรามีผลรวมของซีรีส์สูงถึง `n`
5. สุดท้าย เราใช้ตัวระบุรูปแบบ `"{:.5f}"` กับเมธอด `format` เพื่อจัดรูปแบบเอาต์พุตเป็นทศนิยมห้าตำแหน่ง

ฉันหวังว่าจะช่วยได้!'''