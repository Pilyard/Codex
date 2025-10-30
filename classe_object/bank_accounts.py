class BankAccount():
    def __init__(self, first_name, last_name, account_Id, account_type, pin, inital_balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_Id
        self.account_type = account_type
        self.pin = pin
        self.balance = inital_balance

    def deposit(self, amount):
        self.balance += amount
        print('You deposited ${} successfully!'.format(amount))
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print('You withdraw ${} successfully!'.format(amount))
        return self.balance

    def display_balance(self):
        return print('Current Account Balance: ${}'.format(self.balance))


my_account = BankAccount('João', 'Pires', 40250, 'Credit/Debit', 2025, 0)

my_account.deposit(96)
my_account.withdraw(25)
my_account.display_balance()
