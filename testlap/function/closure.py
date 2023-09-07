
# def urban(city):
#     global max_pop, min_pop, pop_sum, n
#     n = 0
#     for name, pop in city.items(): 
#         if pop > max_pop:
#             max_pop = pop
#         if pop < min_pop:
#             min_pop = pop
#         pop_sum += pop
#         n += 1
#     print('maximum population:', max_pop)
#     print('minimum population:', min_pop)
#     print('difference between maximum and minimum population:', max_pop - min_pop)
#     print('average population:', pop_sum / n)
# max_pop = 0
# min_pop =1000000
# pop_sum = 0
# city_pop = {'A':9765, 'B':3441, 'C':2954, 'D':1531 } 
# urban(city_pop)
# x=10
# y=11
# def foo():
#     x=20
#     def bar():
#         a=30
#         print(a,x,y)
#     bar()
#     x=40
#     bar()
# foo()

# def print_counter():
#     global counter 
#     counter = 200
#     print('counter', counter)
# counter = 100
# print_counter()
# print('counter', counter)

# def callfucn(fucn):
#     fucn()
# def gree():
#     print("hello")

# print('callfucn(greet)function call')
# callfucn(gree)#ການເອີ່້ນຟັງຊັ່ນມາໃຊ້

# def plus(a, b):
#     return a + b
# def minus (a, b):
#     return a - b
# l_list = [plus, minus]
# a = l_list[0] (100, 200)
# b = l_list[1] (100, 200)
# print('a =', a)
# print('b=', b)


# def add(a, b):
#     return a + b
# def f(g, a, b): 
#     return g(a,b) 
# print(f(add, 3, 4))

# def decorate(style= 'italic'): 
#     def italic(s):
#          return '<i>'+s+ '</i>'
#     def bold(s):
#         return '<b>'+s+ '</b>'
#     if style == 'italic':
#         return italic
#     else:
#         return bold
# dec =decorate() 
# print (dec('hello'))
# dec2 = decorate('bold')
# print(dec2('hello'))

# def greeting():
#     def say_hi():
#         print('hello')
#     say_hi()
# greeting()


# def calc():
#     a = 3
#     b = 5
#     def mul_add(x):
#         return a*x + b
#     return mul_add
# num = calc()
# print(num(3))

# def calc():
#     a = 3
#     b = 5
#     mul_add = lambda x: a*x + b
#     return mul_add
# num = calc()
# print(num(3))

lst= [ x for x in range(1,101)]
def func1(a):
    def func2():
        result1 = []
        for i in a:
            if i % 5 == 0:
                result1.append(i)
        return result1
    def func3():
        result2 =[]
        for i in a: 
            if i % 7 == 0:
                result2.append(i)
        return result2
    lst = sorted(set(func2()+func3()))
    return lst
print(lst)
print(func1(lst))
