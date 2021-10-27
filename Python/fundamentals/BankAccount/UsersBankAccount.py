class BankAccount:
    all_accounts = []
    def __init__(self, balance = 0, percentage = .015) -> None:
        self.account_balance = balance
        self.interest_rate = percentage
        BankAccount.all_accounts.append(self)

    def deposit_funds(self, amount) -> int:
        self.account_balance += amount

    def make_withdrawl(self, amount) -> int:
        if self.account_balance > amount + 5:
            self.account_balance -= amount
            print('deducting 5 dollar charge fee')
            self.account_balance -= 5
        else:
            print("insufficent funds")

    def display_account_info(self):
        print(self.account_balance)

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.interest_rate)

    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f'Account Balance: {account.account_balance}, Interest Rate: {account.interest_rate}')


class User:
    def __init__(self,name,email) -> str:
        self.name = name
        self.email = email
        self.account = BankAccount(balance=0,percentage = .015)

    def deposit(self,amount : int) -> '$':
        self.account.deposit_funds(amount)

    def withdraw(self,amount : int) -> '$':
        self.account.make_withdrawl(amount)

    def display_balance(self):
        print(f"{self.name}'s account balance is {self.account.account_balance}")

    def interest_gains(self):
        self.account.yield_interest()

    def transfer_money(self,other_user : str,amount : int ):
        if self.account.account_balance >= amount:
            self.account.account_balance -= amount
            other_user.account.account_balance += amount
        else:
            print('Transaction rejected. Insufficient funds')


Jeff = User('Jeff','jeff@clap.com')
Jeff.deposit(500)
Jeff.display_balance()
Jeff.withdraw(50)
Jeff.display_balance()
Jeff.interest_gains()
Jeff.display_balance()