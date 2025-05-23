menu = """
    Welcome to the ItaBank =] 
    
    Please choose press a digit and choose your option:
    
    [d] Deposit
    [w] Withdraw
    [s] Check statement
    [q] Quit
"""
balance = 0.0
daily_limit = 500

statement = ""
withdraw_counting = 0
COUNT_WITHDRAW_DAY = 3


"""Fuction that implements deposit operation under following rules:
    - Only possible to withdraw positive amounts.

    - All deposits should be stored in one variable and view in the 
    view statement operation.
"""
def do_deposit(_dep_amout):
    if dep_amount <= 0:
        print("The amout to deposit should be positive!")
        print("Operation not conclude!")
        exit
    balance += dep_amount
    statement += f""" \nDeposit of: $ {dep_amount}. 
                      New balance: {balance} """ 
    
    print(f"Deposit of /$ { dep_amount } succesfully done! ")


"""Fuction that implements withdraw operation under following rules:
    -  Only 3 withdraws per day.

    - Withdraw daily limit $500.

    - If there is no balance the system abort the withdraw operation and send a message.
"""
def do_withdraw(_with_amount):
    if withdraw_counting >= 3:
        print("Daily count for withdraw reached")
        exit
  
    if _with_amount >= daily_limit:
        print(f"Only withdraw until ${daily_limit} are permited!")
        exit
    
    if balance < _with_amount:
        print(f" Amount for withdraw ${daily_limit} is major then the account balance ${balance}!")
        exit   
    
    balance += _with_amount
    withdraw_counting += 1
    statement += f""" \nWithdraw of: $ {_with_amount}. 
                New balance: {balance} """    

def check_statememt():
    print("Here the statment of your account: ")
    print(statement)

while True:

    option = input(menu)

    if option == "d":
        message_deposit = "Please inform the amount for deposit: "
        dep_amount = input(message_deposit)
        do_deposit(dep_amount)
    
    elif option == "w":
        message_withdraw = "Please inform the amount for withdraw: "
        with_amount = input(message_withdraw)
        do_deposit(with_amount)
        

    elif option == "s":
        check_statememt()
        
    elif option == "q":
        print("Bye!")
    else:
        print(" Please choose one option from the menu ;]")