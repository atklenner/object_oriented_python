from Bank import *

bank = Bank()

joe_account_number = bank.create_account('Joe', 100, 'JoesPassword')
print("Joe's account number is:", joe_account_number)
mary_account_number = bank.create_account('Mary', 12345, 'MarysPassword')
print("Mary's account number is:", mary_account_number)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0] # grab the first letter
    print()
    if action == 'b':
        bank.balance()
    elif action == 'c':
        bank.closeAccount()
    elif action == 'd':
        bank.deposit()
    elif action == 'o':
        bank.openAccount()
    elif action == 's':
        bank.show()
    elif action == 'q':
        break
    elif action == 'w':
        bank.withdraw()
    else:
        print('Sorry, that was not a valid action. Please try again.')
    print('Done')