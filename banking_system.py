def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest."""
    return (principal * rate * time) / 100


# Initialize user's account balance
balance = 0

# Bank operation
while True:
    print("""
Welcome to the Simple Bank!
1. Deposit Money
2. Withdraw Money
3. View Balance and Calculate Interest
4. Exit
""")
    
    choice = int(input("Choose an option (1-4): "))
    
    if choice == 1:  # Deposit Money
        deposit = float(input("Enter the amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print(f"Successfully deposited {deposit:.2f}. Your new balance is {balance:.2f}.")
        else:
            print("Deposit amount must be greater than zero.")
    
    elif choice == 2:  # Withdraw Money
        withdrawal = float(input("Enter the amount to withdraw: "))
        if 0 < withdrawal <= balance:
            balance -= withdrawal
            print(f"Successfully withdrew {withdrawal:.2f}. Your new balance is {balance:.2f}.")
        else:
            print("Invalid withdrawal amount. Please ensure it is within your current balance.")
    
    elif choice == 3:  # View Balance and Calculate Interest
        print(f"Your current balance is {balance:.2f}.")
        
        # Assuming 5 years and 4% rate of interest
        time = 5
        rate = 4
        accrued_interest = calculate_simple_interest(balance, rate, time)
        original_principal = balance - accrued_interest
        
        print(f"""
Account Summary:
- Current Balance: {balance:.2f}
- Time Saved: {time} years
- Accrued Interest: {accrued_interest:.2f}
- Original Principal: {original_principal:.2f}
        """)
    
    elif choice == 4:  # Exit
        print("Thank you for banking with us! Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
