def main():
    """Main function to run the banking application."""
    print("WELCOME TO MZ BANK!")
    
    # The balance is managed here, in the main scope.
    balance = 0.00
    
    # The main menu loop
    while True:
        print("\n********** MAIN MENU **********")
        print("\n1: Check Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Exit")
        
        choice = input("Action: ")
        
        if choice == "1":
            # Just show the balance. No change is needed.
            check_balance(balance)
        elif choice == "2":
            # This function will return the NEW balance, so we update it here.
            balance = deposit(balance)
        elif choice == "3":
            # This function will also return the NEW balance.
            balance = withdraw(balance)
        elif choice == "4":
            print("\n*****Have a Good day*****")
            break
        else:
            print("\nInvalid Action number! Please choose a number from 1 to 4.".title())

def check_balance(current_balance):
    # Displays the current balance.
    print(f"\nBalance: ${current_balance:.2f}")

def deposit(current_balance):
    # Handles the deposit logic and returns the new balance.
    print() # Add a space for readability
    amount = float(input("Deposit Amount: "))
    
    if amount <= 0:
        print("\nInvalid deposit amount. Must be a positive number.".title())
        return current_balance # Return the original balance without changing it
    else:
        new_balance = current_balance + amount
        print(f"\nSuccessful deposit. Your new balance is ${new_balance:.2f}")
        return new_balance # Return the calculated new balance

def withdraw(current_balance):
    # Handles the withdrawal logic and returns the new balance.
    print() # Add a space for readability
    amount = float(input("Withdrawal Amount: "))
    
    if amount <= 0:
        print("\nInvalid withdrawal amount. Must be a positive number.".title())
        return current_balance # Return original balance
    elif amount > current_balance:
        print("\nInsufficient Funds".title())
        return current_balance # Return original balance
    else:
        new_balance = current_balance - amount
        print(f"\nSuccessful withdrawal. Your new balance is ${new_balance:.2f}")
        return new_balance # Return the calculated new balance

# Call the main function to start the program
main()
