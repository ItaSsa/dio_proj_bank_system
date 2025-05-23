menu = """
    Welcome to the ItaBank =] 
    
    Please choose press a digit and choose your option:
    
    [d] Deposit
    [w] Withdraw
    [s] Check statement
    [q] Quit
"""
balance = 0
daily_limit = 500
statement = ""
withdraw_counting = 0
COUNT_WITHDRAW_DAY = 3


"""Fuction that implements deposit operation under following rules:
    - Only possible to withdraw positive amounts.

    - All deposits should be stored in one variable and view in the 
    view statement operation.
"""
def do_deposit(dep_amout):
    if dep_amount <= 0.0:
        print("The amount to deposit should be positive!")
        print("Operation not conclude!")
        exit
    global balance 
    balance +=  dep_amount

    global statement
    statement += f"""{"-"*70} \nDeposit of: $ {dep_amount}.\n  New balance: {balance}\n""" 
    
    print(f"Deposit of $ { dep_amount } succesfully done! ")


"""Fuction that implements withdraw operation under following rules:
    -  Only 3 withdraws per day.

    - Withdraw daily limit $500.

    - If there is no balance the system abort the withdraw operation and send a message.
"""
def do_withdraw(with_amount):
    global balance,withdraw_counting,statement

    if withdraw_counting >= 3:
        print("Daily count for withdraw reached")
        exit
  
    if with_amount >= daily_limit:
        print(f"Only withdraw until ${daily_limit} are permited!")
        exit
    
    if balance < with_amount:
        print(f" Amount for withdraw ${daily_limit} is major then the account balance ${balance}!")
        exit   
    
    balance -= with_amount
    withdraw_counting += 1
    statement += f"""{"-"*70} \nWithdraw of: $ {with_amount}. \n  New balance: {balance}\n """

def check_statememt():
    global statement
    print("Here the statment of your account: ")
    print(f"Actual balance: ${balance} ")
    print("-"*70)
    print(f"History: ")
    print(statement)

while True:

    option = input(menu)

    if option == "d":
        message_deposit = "Please inform the amount for deposit: "
        dep_amount = float(input(message_deposit))
        do_deposit(dep_amount)
    
    elif option == "w":
        message_withdraw = "Please inform the amount for withdraw: "
        with_amount = float(input(message_withdraw))
        do_withdraw(with_amount)


    elif option == "s":
        check_statememt()
        
    elif option == "q":
        print("Bye!")
        break

    else:
        print(" Please choose one option from the menu ;]")