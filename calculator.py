def add(num1,num2):
    result=num1+num2
    print(num1,"+",num2,"=",result)
def sub(num1,num2):
    result=num1-num2
    print(num1,"-",num2,"=",result)
def multi(num1,num2):
    result=num1*num2
    print(num1,"*",num2,"=",result)
def div(num1,num2):
    result=num1/num2
    print(num1,"/",num2,"=",result)
choice=input("enter operator: +,-,*,/: ")
firstnum=int(input("enter your first number: "))
secondnum=int(input("enter your second number: "))
if choice=="+":
    add(firstnum,secondnum)
if choice=="-":
    sub(firstnum,secondnum)
if choice=="*":
    multi(firstnum,secondnum)
if choice=="/":
    div(firstnum,secondnum)