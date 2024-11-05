num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
operation = input("Enter Operations (+,-,*,/: ")

if operation == '+':
    result = num1+num2
elif operation == '-':
    result = num1-num2
    
elif operation == '*':
    result = num1*num2
elif operation == '/':
    if operation != 0:
        result = num1/num2
    else:
        print("Error! Division by zero ")
else:
    print("Invalid operation")
    
print( "Result is ", result)    
    
    
    
