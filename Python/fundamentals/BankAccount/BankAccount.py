class BankAccount:
    def __init__(self, bank, balance = 0, percentage = .015) -> None:
        self.bank = bank
        self.account_balance = balance
        self.interest_rate = percentage

    def deposit(self, amount) -> int:
        self.account_balance += amount

    def withdraw(self, amount) -> int:
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

USAA = BankAccount('USAA', 1000, .01)
Navy_Fed = BankAccount('Navy Fed',5000)

USAA.deposit(250)
USAA.deposit(50)
USAA.deposit(815)
USAA.withdraw(660)
USAA.yield_interest()
USAA.display_account_info()
print('\n')

Navy_Fed.deposit(250)
Navy_Fed.deposit(500)
Navy_Fed.withdraw(75)
Navy_Fed.withdraw(115)
Navy_Fed.withdraw(30)
Navy_Fed.withdraw(80)
Navy_Fed.yield_interest()
Navy_Fed.display_account_info()
print('\n')
