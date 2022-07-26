# ATM Application

ElonsAccount = {
    'name': 'Elon Musk',
    'accountNo': '18885183752',
    'balance': 1000,
    'adAccount': 2000
}
DogesAccount = {
    'name': 'Doge Cute',
    'accountNo': '46729090227',
    'balance': 10000,
    'adAccount': 5001
}


def query_balance(account):
    print(
        f"There is a total balance of {account['balance']} USD in your bank account number {account['accountNo']}. Also your addition account balance is {account['adAccount']} USD")


def withdraw(account, amount):
    print(f'Hello {account["name"]}')
    if account['balance'] > amount:
        account['balance'] -= amount
        print('You can withdraw your money.')
        query_balance(account)
    else:
        summary = account['balance'] + account['adAccount']
        if summary > amount:
            useAdAccount = str(input('Would you use your addition account for withdrawing money? (y/n)'))
            if useAdAccount == 'y':
                account['adAccount'] = account['adAccount'] - (amount - account['balance'])
                account['balance'] = 0
                print('You can withdraw your money.')
                query_balance(account)
            else:
                query_balance(account)
                print('Your process canceled according to your selection. Goodbye!')
        else:
            print('Unfortunately your balance is not enough for your withdraw process. Try again later.')
            query_balance(account)


withdraw(ElonsAccount, 2000)
