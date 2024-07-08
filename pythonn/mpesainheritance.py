class Account:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        if amount >0:
            self.balance=self.balance+amount
            print(f"{amount} deposited successfully.New balance is {self.balance}")
        else:
            print("Amount should be greater than zero")

    def withdraw(self,amount):
        if amount >self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn successfully.New balance is {self.balance}")
    def __str__(self):
        return f"Account holder: {self.account_holder}\n Balance: {self.balance}"
class SavingsAccount(Account):
    def __init__(self,account_holder,balance,interest_rate):
        super().__init__(account_holder,balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        interest=self.balance*self.interest_rate
        self.balance=self.balance+interest
        print(f"Interest added successfully. New balance is {self.balance}")
    def __str__(self):
        return (f"Savings Account Holder: {self.account_holder}\nBalance: "
                f"{self.balance},interest rate: {self.interest_rate}")
account=Account("lew",1000)
account.deposit(100)
account.withdraw(500)
print(account)
savings=SavingsAccount('jAQN',1000,14)
savings.deposit(500)
savings.withdraw(300)
savings.add_interest()
print(savings)


