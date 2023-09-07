# import math
# x1=input("Enter the X1: ")
# y1=input("Enter the y1: ")
# x2=input("Enter the x2: ")
# y2=input("Enter the y2: ")
# def distance(x1, y1, x2, y2):
#       return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
# distance = distance(float(x1), float(y1), float(x2), float(y2))
# print('The distance between two points: ',distance)


# n_list=[10,20,30]
# lsit1= list(map(lambda x:x*2,n_list))
# lsit2= list(map(lambda x:x*3,n_list))
# print(' twice the inpu values: ',lsit1)
# print('Three times the input values: ',lsit2)



# class Vector2D:
#     def __mult__(self,v1,v2):
#         self.v1=v1
#         self.v2=v2

#     def get_mul(self):
#         return self.mul
#     def get_Division(self):
#         return self.Division
#     def __truediv__(self,v1,v2):
#         self.v1=v1
#         self.v2=v2

# v
# v=Vector2D(10,20)
# print(v.get_mul())
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector2D(x, y)
    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Vector2D(x, y)
    def __repr__(self):
        return f"({self.x}, {self.y})"
v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
result_mul = v1 * v2
print("V1 * V2 =", result_mul)
result_div = v1 / v2
print("V1 / V2 =", result_div)

def is_palindrome(number):
    if number[0] != number[-1]:
        return f"This is not palindrome."
    else:
        return f"This is palindrome."
number = input("Enter a string: ")
print(is_palindrome(number))