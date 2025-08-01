# a=int(input("enter math no."))
# b=int(input("enter english no."))
# a=5
# b=10
# c=a+b
# if c==50:
#     print("pass")
# else:
#     print("fail")


    ##pass faill by number
a=int(input("enter math no."))
b=int(input("enter english no."))
if a+b==50:
    print("pass")
else:
    print("fail") 


##odd even
# a=int(input("enter first number"))
# if a % 2==0:
#     print("Number is even")
# else:
#     print("number is odd")


a=int(input("enter your marks"))
if a>=90:
    print("grade a")
elif a>=75:
    print("grade b")
elif a>=60:
    print("grade c")
elif a<60 and a>40:
    print("grad d")
else:
    print("pass")
    
##check if its a leap year or not

a=int(input('Enter the year'))
if a%4==0 and a%100!=0:
    print(f'{a} as leap year')
elif a%400==0:
    print(f'{a} as leap year')
else:
    print(f'{a} is not a leap year')

##