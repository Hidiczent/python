calclulate=input("1 addition, 2 Subtraction 3 mutiplecation 4Division: ")
a=int(input("Enter number1 :"))
b=int(input("Enter number2:"))
a=int(a)
b=int(b)

if calclulate == 1:
    result=a+b
    print(a,"+",b,'=',result)
elif calclulate==2:
    result = a-b
    print(a,"-",b,'=',result)
elif calclulate==3:
    result= a*b
    print(a,"*",b,'=',result)
elif calclulate==4:
    result = a/b
    print(a,"/",b,'=',result)
