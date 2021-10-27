class User:
    def __init__(self,name,email) -> str:
        self.name = name
        self.email = email
        self.account_balance = 0

    def deposit(self,amount : int) -> '$':
        self.account_balance += amount

    def make_withdrawl(self,amount : int) -> '$':
        self.account_balance -= amount

    def display_balance(self):
        print(f"{self.name}'s account balance is {self.account_balance}")

    def transfer_money(self,other_user : str,amount : int ):
        if self.account_balance >= amount:
            self.account_balance -= amount
            other_user.account_balance += amount
        else:
            print('Transaction rejected. Insufficient funds')



Jeff = User('jeff','jeff@clap.com')
Sarah = User('sarah','sarah@clap.com')
Emma = User('emma','emma@clap.com')

Jeff.deposit(100)
Jeff.deposit(150)
Jeff.deposit(50)
Jeff.make_withdrawl(200)
Jeff.display_balance()
print('\n')

Sarah.deposit(300)
Sarah.transfer_money(Jeff,500)
Sarah.deposit(400)
Sarah.make_withdrawl(30)
Sarah.make_withdrawl(70)
Sarah.display_balance()
print('\n')

Emma.deposit(1000)
Emma.make_withdrawl(450)
Emma.make_withdrawl(400)
Emma.make_withdrawl(50)
Emma.display_balance()
print('\n')

Sarah.transfer_money(Emma,500)
Emma.display_balance()
Sarah.display_balance()
Jeff.display_balance() 