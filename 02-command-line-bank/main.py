# command line, text based, simple Bank. or ATM machine.
# welcome.
# choose the language.
# menu: Check Balance, Withdraw, Deposit, Exit
print("WELLCOME TO MZ BANK!")

def main():
    user_language()
    main_menu()

balance = 0.00
    
def user_language():
    while True: # finding user's preferable language.
        print("please choose a language?".title())
        print("1: English", "2: French", "3: Arabic", sep=" " * 3)
        language = input("language: ".title())
        if language == "1" or language == "2" or language == "3":
             break
        else:
            print("invalid language number!".title())
            continue

def main_menu():
    global balance     # this reminds that any variable inside is reffered to the global one.
    while True:
        print()
        print("********", "MAIN MENU", "********")
        print()
        print("Please choose your Action".title())
        print()
        print("Check Balance   1")
        print("Withdraw        2")
        print("Deposit         3")
        print("Exit            4")
        action = int(input("Action: "))
        
        if action == 1:        # Balance
            print()
            print("Balance:", f"{balance:.2f}")

            continue
        elif action == 2:      # Withdrawal actiod
            while True:
                print()
                withdrawal = float(input("Withdrawal Amount: "))   # Ask for withdrawal Amount
                withdrawal = round(withdrawal, 2)
                if withdrawal <= 0.00:                   # if the number in invalid
                    print()
                    print("invalid Withdrawal amount.".title())
                    continue
                elif withdrawal > balance:      # if we don't have enough balance for withdrawal
                    print()
                    print("Insufficient Funds".title())
                    print()
                    print("Main menu   1".title())
                    print("Withdrawal  2".title())
                    print()
                    menu_withdrawal = int(input("Action: "))
                    if menu_withdrawal == 1:
                        break
                    elif menu_withdrawal == 2:
                        continue
                    else:
                        print("Invalid Action!")
                        continue
                else:
                    print()
                    print("Successful withdrawal.".title())
                    balance = balance - withdrawal
                    break
        elif action == 3:        
            while True:
                print()
                deposit = float(input("deposit Amount: ".title()))     # Ask for Deposit Amount
                deposit = round(deposit, 2)
                if deposit <= 0.00:
                    print()
                    print("invalid deposit amount.".title())
                    continue
                else:
                    print()
                    print("Successful deposit.".title())
                    balance = deposit + balance
                    break
        elif action == 4: 
            print()
            print("******Have a Good day******")
            break
        else:
            print("invalid Action number!".title())
            continue
    
main()
