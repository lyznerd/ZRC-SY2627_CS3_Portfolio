#Activity 3: BankAccount Class

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative.")

# sample Bank Account object
account = BankAccount("0711202667", 3000)

# account information
print("Account Number:", account.account_number)
print(f"Balance: P{account.balance:.2f}")

# update account number
account.account_number = "0711202668"
print("Updated Account Number:", account.account_number)

# update balance
account.balance = 5000
print(f"Updated Balance: P{account.balance:.2f}")

# test balance validation
account.balance = -1000
print(f"Balance: P{account.balance:.2f}")
