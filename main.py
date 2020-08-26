from account import Bank_account

account_26001001010 = Bank_account(1000, 'USD', 26001001010, 'Tom Smith', 'Private Bank', 123456)

choice = int(input('\t\tSelect your action number:'
                   '\n1. View balance'
                   '\n2. View info about account'
                   '\n3. Take money'
                   '\n4. Put money'
                   '\n5. Forecasting the amount of the deposit'
                   '\nENTER NUMBER = '))

if choice == 1:
    balance = account_26001001010.get_account_amount()
    currency = account_26001001010.get_account_currency()
    print('Your balance: ', balance, currency)

elif choice == 2:
    account_26001001010.display_info_bank_account()

elif choice == 3:
    take_amount = int(input('Enter the amount: '))
    amount_account = account_26001001010.get_account_amount() - take_amount
    print('New balance: ', amount_account)

elif choice == 4:
    put_amount = int(input('Enter the amount: '))
    amount_account = account_26001001010.get_account_amount() + put_amount
    print('New balance: ', amount_account)

elif choice == 5:
    money = account_26001001010.get_account_amount()
    month = int(input("Enter month: "))
    rate = int(input("Enter rate(%): "))
    for i in range(1, month + 1):
        money = round(money + money * rate / 100 / 12, 2)
    print('Forecasting amount: ', money)
