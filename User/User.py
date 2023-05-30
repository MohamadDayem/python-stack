class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount	
    def make_withdraw(self, amount):	
        self.account_balance -= amount
    def display_user_balance(self):
        name= self.name
        balance=self.account_balance
        print(f'user : {name}, balance: ${balance}')

        

oday = User('mohamad', 'fefawd@ioshk.com')
awad = User('Awad','awadshfv@maidl.com')
saleh = User('Saleh','saleshbb@jgdkj.com')

awad.make_deposit(500)
awad.make_deposit(200)
awad.make_withdraw(500)
awad.make_withdraw(100)
awad.display_user_balance()

oday.make_deposit(600)
oday.make_deposit(400)
oday.make_withdraw(200)
oday.make_withdraw(150)
oday.display_user_balance()

saleh.make_deposit(600)
saleh.make_withdraw(150)
saleh.make_withdraw(300)
saleh.make_withdraw(100)
saleh.display_user_balance()
