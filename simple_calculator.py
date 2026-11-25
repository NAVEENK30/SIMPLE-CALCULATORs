
num1=int(input("Enter your number1:"))
num2=int(input("Enter your number2"))

opration=input("enter the opertions:")

if opration == "add" or "+" :
    c=num1+num2
    print(c)

elif opration == "sub" or "-" :
    c=num1-num2
    print(c)

elif opration == "mul" or "*" :
    c=num1*num2
    print(c)

elif opration == "div" or "/" :
    c=num1/num2
    print(c)

else:
    print("its not an operator")