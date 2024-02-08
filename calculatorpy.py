print("this is a program for simple arthemetic calculator ")
a=int(input("give ur first number "))
b=int(input("give ur second number "))
c=input("give the operator ")
if c=="+" :
    print("your result for addition is ", a+b)
elif c=="-" :
    print("your result for subtraction is ", a-b)
elif c=="*" :
    print("your result for multipication is ", a*b)
elif c=="/" :
    print("your result for division is ", a/b)    
elif c=="%" :
    print("your remainder for division is ", a%b,'and your quotient is ',a//b)  
else 
    print("your opreator is wrong ,retry")     