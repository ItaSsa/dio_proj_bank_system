menu = """
    Welcome to the ItaBank =] 
    
    Please choose press a digit and choose your option:
    
    [d] Deposit
    [w] Withdraw
    [s] View statement
    [u] Create Users
    [l] List users
    [q] Quit
"""
balance = 0
daily_limit = 500
statement = ""
withdraw_counting = 0
TOTAL_WITHDRAW_DAY = 3
users = []
accounts = []

def create_user(users,*,name, birth_date, id, adress):
    if any(user["id"] == id for user in users):
        raise ValueError(" Already have a user with this ID.")
        return users
    
    user = {
        "name": name,
        "birth_date": birth_date,
        "id": id,
        "adress":adress
    }
    
    users.append(user)
     
    return users

def create_check_account():
    pass

def list_users(users):
    print("Users: ")
    
    for user in users:
        for k,v in user.items():
            print(f"{k} : { v }")
    

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


def do_withdraw(*,balance, statement, value, daily_limit,
                total_withdraw, withdraw_counting):
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


def view_statememt(balance,*, statement):
    """
    Function view_statement
    """

    print("-"*70)
    print("Here the statment of your account: ")
    print("-"*70)
    print("-"*70)
    print(f"Actual balance: ${balance} ")
    print("-"*70)
    print("-"*70)
    print(f"History: ")
    return balance,statement


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
        balance,statement = view_statememt(balance,statement = statement)

        print(statement)
    
    elif option == 'u':
        var_input = input("Inform name, birth_date, id and adress (separated by commas): ")

        i_name, i_birth_date, i_id, id_adress = var_input.split(",")

        users = create_user(users,name = i_name, birth_date = i_birth_date, id = i_id, adress = id_adress)
        
        print("User included succesfully!")

    elif option == 'l':
        list_users(users)

    elif option == "q":
        print("Bye!")

        break

    else:
        print(" Please choose one option from the menu ;]")