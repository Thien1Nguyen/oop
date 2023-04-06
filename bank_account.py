"""
If you imagine a banking system, and how the data is modeled, you may think, well, everything should be tied to the customer, in other words, the user. But users have accounts, and accounts have balances. This gives us the idea that maybe an account is its own class apart from the user class. But as we stated, it is not completely independent of the User class; accounts only exist because users open them.

For this assignment, don't worry about putting any user information in the BankAccount class. We'll take care of that in the next lesson!

Let's first just get some more practice writing classes by writing a new BankAccount class.

The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

The class should also have the following methods:

deposit(self, amount) - increases the account balance by the given amount
withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
display_account_info(self) - print to the console: eg. "Balance: $100"
yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
This means we need a class that looks something like this:
"""
class BankAccount:
    # don't forget to add some default values for these parameters!
    account_name = "Unknown"
    balance = 0
    int_rate = 0
    accounts =[] # creating a list of bank accounts

    def __init__(self, account_name, int_rate, balance):
        self.account_name = account_name # added a name attribute to make the display of NINJA BONUS more clear
        self.int_rate = int_rate
        self.balance = balance
        self.accounts.append(self)

    def display_into(self):
        print(f"account name:{self} \ninterst rate: {self.int_rate} \nbalance: {self.balance} ")
    
    def deposit(self, amount):  #a method to deposit into the account
        if amount > 0:
            self.balance += amount
            return self
        else:
            print("You can't take money out during a deposit!")
            return self
        
    def withdraw(self, amount): #a method to withdraw from the account
        if (amount > 0) and (self.balance >= amount ):
            self.balance -= amount
            return self
        elif amount < 0:
            print("You can't put in money while withdrawing!")
            return self
        elif amount > self.balance:
            print("Not enough funds!")
            return self
    def display_account_info(self): # a method to check the account's balance
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self): # a method to add interest to the balance
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print(f"New balance with interest: ${self.balance}")
            return self
        else:
            print("Can't yield interest when the balance is negative!")
            return self
        
    @classmethod
    def all_account_display(cls):
        for account in cls.accounts:
            print(f"{account.account_name} \n interest rate: {account.int_rate} \n balance: ${account.balance}")



other_account = BankAccount("other_account", 0.10, 70)

my_account = BankAccount("my_account", 0.01, 120000000)

#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
other_account.deposit(10).deposit(20).deposit(25).withdraw(60).display_account_info().yield_interest().display_account_info()  
#To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
my_account.deposit(1).deposit(2).withdraw(1200000).withdraw(300000).withdraw(100).withdraw(12).display_account_info().yield_interest().display_account_info()

#Ninja Bonus, a class method to print all instances of a Bank Account's info
BankAccount.all_account_display()