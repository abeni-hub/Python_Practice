
count = 0
while True:
    
    # Ask the user how many number they want
    number_chain = int(input("Enter the series of numbers"))
    
    # print the chain of number starting from the current_numbers
    
    for i in range(count , count + number_chain):
        print(i)
    
    
    # update the current number to continue from the last printed number    
    count +=number_chain    
    
    # Ask the user if they want to continue
    continue_number = input("Would you like to continue?Y/N")
    
    #keep the chain running by inputting a new number and starting a new count from 0 to the new user-input number
    if continue_number == "Y":
        continue
    
    # exit the application
    if continue_number == "N":
        break
    
