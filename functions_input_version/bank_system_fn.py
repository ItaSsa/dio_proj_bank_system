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
TOTAL_WITHDRAW_DAY = 3
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
        return balance, statement 

    balance +=  value

    statement += f"""{"-"*70} \nDeposit of: $ {value}.\n  New balance: {balance}\n""" 
    
    print(f"Deposit of $ { value } succesfully done! ")

    return balance, statement


def do_withdraw(balance=0, statement="", value=0, daily_limit=0,
                total_withdraw=0, withdraw_counting=0):
    """Fuction that implements withdraw operation under following rules:
        -  Only 3 withdraws per day.

        - Withdraw daily limit $500.

        - If there is no balance the system abort the withdraw operation and send a message.
    """

    if withdraw_counting >= total_withdraw:
        print("Daily count for withdraw reached")
        return balance, statement, withdraw_counting
  
    if value >= daily_limit:
        print(f"Only withdraw until ${daily_limit} are permited!")
        return balance, statement, withdraw_counting
    
    if balance < value:
        print(f" Amount for withdraw ${daily_limit} is major then the account balance ${balance}!")
        return balance, statement, withdraw_counting 
    
    balance -= value

    withdraw_counting += 1
    
    statement += f"""{"-"*70} \nWithdraw of: $ {value}. \n  New balance: {balance}\n """

    return balance, statement, withdraw_counting


def check_statememt():
    """
    Function view_statement

    @args: positional: balance , keyword: statement
    """
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
        
        value = float(input(message_withdraw))
        
        balance, statement, withdraw_counting = do_withdraw(balance=balance, statement=statement, value=value, daily_limit=daily_limit,
                total_withdraw=TOTAL_WITHDRAW_DAY, withdraw_counting=withdraw_counting)


    elif option == "s":
        check_statememt()
        
    elif option == "q":
        print("Bye!")
        break

    else:
        print(" Please choose one option from the menu ;]")