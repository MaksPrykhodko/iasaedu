class Bank_account:


    def __init__(self, account_amount, account_currency, account_number, account_owner, account_bank, mfi_bank):    #constructor
        self.__account_amount = account_amount          #account balance
        self.__account_currency = account_currency      #account currency
        self.__account_number = account_number          #number of account
        self.__account_owner = account_owner            #name, surname
        self.__account_bank = account_bank              #name of bank
        self.__mfi_bank = mfi_bank                      #mfi_bank - code of bank


    def get_account_amount(self):           #func get account_amount
        return self.__account_amount

    def get_account_currency(self):         #func get account_currency
        return self.__account_currency

    def get_account_number(self):           #func get account_number
        return self.__account_number

    def get_account_owner(self):            #func get account_owner
        return self.__account_owner

    def get_account_bank(self):             #func get account_bank
        return self.__account_bank

    def get_mfi_bank(self):                 #func get mfi_bank
        return self.__mfi_bank


    def set_account_amount(self, value_account_amount):         #func set account_amount
        if value_account_amount > 0:
            self.__account_amount = value_account_amount
        else:
            print("ERROR account amount")

    def set_account_currency(self, value_account_currency):     #func set account_currency
        if value_account_currency in range('USD', "EURO"):
            self.__account_currency = value_account_currency
        else:
            print("Currency not found")

    def set_account_number(self, value_account_number):         #func set account_number
        if value_account_number > 0:
            self.__account_number = value_account_number
        else:
            print("ERROR account number")

    def set_account_owner(self, value_account_owner):           #func set account_owner
        self.__account_owner = value_account_owner

    def set_account_bank(self, value_account_bank):             #func set account_bank
        self.__account_bank = value_account_bank

    def set_mfi_bank(self, value_mfi_bank):                     #func set mfi_bank
        self.__mfi_bank = value_mfi_bank


    def display_info_bank_account(self):                                #func view info about account
        print('\t\tINFO ABOUT BANK ACCOUNT: ', '\n',
              'Account amount = ', self.__account_amount, '\n',
              'Account currency is: ', self.__account_currency, '\n',
              'Account number is: ', self.__account_number, '\n',
              'Account owner is: ', self.__account_owner, '\n',
              'Account bank is: ', self.__account_bank, '\n',
              'MFI bank is: ', self.__mfi_bank, '\n')
