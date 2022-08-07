from Bank import *

bank = Bank()

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
    action = action[0]  # grab the first letter
    print()
    try:
        if action == 'b':
            bank.balance()
        elif action == 'c':
            bank.close_account()
        elif action == 'd':
            bank.deposit()
        elif action == 'o':
            bank.open_account()
        elif action == 's':
            bank.show()
        elif action == 'q':
            break
        elif action == 'w':
            bank.withdraw()
    except AbortTransaction as error:
        print(error)

print('Done')
