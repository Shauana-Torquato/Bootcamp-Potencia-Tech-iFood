menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[4] Close

=> """

balance = 0
limit = 500
statement = ""
number_withdraws = 0
LIMIT_WITHDRAWS = 3

while True:
    
    option = input(menu)

    if option == "1":
            value = float (input("Enter the amount for deposit: "))

            if value > 0 :
                balance += value
                statement += f"Deposit: BRL {value:.2f}\n"
                print ("The entered amount was succesfully deposited")
    
            else :
                print ("Invalid operation! The entered amount is not valid")

    elif option == "2":
            value = float (input("Enter the amount for withdraw: "))

            exceeded_balance = value > balance
            exceeded_limit = value > limit
            exceeded_withdraws = number_withdraws >= LIMIT_WITHDRAWS

            if exceeded_balance:
                  print ("Operation Not Valid! The balance is not enough to conclude the operation")
            elif exceeded_limit:
                  print ("Operation Not Valid! The requested amount for the withdraw exceeded the daily limit")

            elif exceeded_withdraws:
                  print ("Operation Not Valid! The maximum possible of withdraws in a day was exceeded")

            elif value > 0:
                  balance -= value
                  statement += f"Withdraw: BRL {value:.2f}\n"
                  print ("The withdraw was successfully concluded")
                  number_withdraws += 1

            else:
                  print("Operation Not Valid! The entered amount is not valid.")

    elif option == "3":
          print ("\n=============== STATEMENT =================")
          print ("This account has no transactions registered." if not statement else statement)
          print (f"\nBalance: R$ {balance:.2f}")
          print ("================================================================")

    elif option == "4":
          break
    
    else:
          print ("The selected operation is not valid! Select a new operation")