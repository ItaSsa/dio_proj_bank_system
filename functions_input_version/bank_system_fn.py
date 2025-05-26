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
users = []

def create_user():
    pass

def create_check_account():
    pass

def list_users():
    pass

def list_acounts():
    pass

def do_deposit( balance, value , statement ):
    """
    Function that implements deposit operation under following rules:
        - Only possible to withdraw positive amounts.
        - All deposits should be stored in one variable and view in the 
        view statement operation.

    """

    if value <= 0.0:
        print("The amount to deposit should be positive!")
        print("Operation not conclude!")
        return

    balance +=  value

    statement += f"""{"-"*70} \nDeposit of: $ {value}.\n  New balance: {balance}\n""" 
    
    print(f"Deposit of $ { value } succesfully done! ")

    return balance, statement


"""Fuction that implements withdraw operation under following rules:
    -  Only 3 withdraws per day.

    - Withdraw daily limit $500.

    - If there is no balance the system abort the withdraw operation and send a message.
"""
def do_withdraw(with_amount):
    #args keyword only balance,statment, value,limit,num_withdraw,limit_withdraw
    # return balance, statment
    global balance,withdraw_counting,statement

    if withdraw_counting >= 3:
        print("Daily count for withdraw reached")
        return
  
    if with_amount >= daily_limit:
        print(f"Only withdraw until ${daily_limit} are permited!")
        return
    
    if balance < with_amount:
        print(f" Amount for withdraw ${daily_limit} is major then the account balance ${balance}!")
        return  
    
    balance -= with_amount
    withdraw_counting += 1
    statement += f"""{"-"*70} \nWithdraw of: $ {with_amount}. \n  New balance: {balance}\n """

"""
    Function view_statement

    @args: positional: balance , keyword: statement
"""
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
        value = float(input(message_deposit))
        balance,statement = do_deposit( balance, value , statement )
    
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