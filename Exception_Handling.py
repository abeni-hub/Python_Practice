# Exception Handling

try:
    a = b
except:
    print('The variable has not been assigned')


# Name Error exception Handling
try:
    a = b

except NameError as ex:
    print(ex)

# Zero Division Error

try:
    a = 10/0

except ZeroDivisionError as ex:
    print(ex)    
    print("please enter the denominator greater than zero")

# Zero Division and Exception
try:
    num = int(input("Enter a number: "))
    result = 10/num

except ZeroDivisionError:
    print("Enter denominator greater than zero")

except ValueError:
    print("Enter a valid number")          

except Exception as ex:
    print(ex)    
    print("Main exception got caught here")      


# try,except,else block
try:
    num = int(input("Enter a number: "))
    result = 10/num

except ZeroDivisionError:
    print("Enter denominator greater than zero")

except ValueError:
    print("Enter a valid number")          

except Exception as ex:
    print(ex)    
    print("Main exception got caught here")      

else:
    print("The division is: ", result)


# try,except,else and finally block
try:
    num = int(input("Enter a number: "))
    result = 10/num

except ZeroDivisionError:
    print("Enter denominator greater than zero")

except ValueError:
    print("Enter a valid number")          

except Exception as ex:
    print(ex)    
    print("Main exception got caught here")      

else:
    print("The division is: ", result)
finally:
    print("The execution is done")

# File Handling and Exception Handling

try:    

    file = open('test.txt', 'r')
    content = file.read()
    print(content)

except FileNotFoundError:
    print("The file does not exist")

finally:
    if 'file' in locals() and not file.closed:
        file.close()        
        print("File is closed")


