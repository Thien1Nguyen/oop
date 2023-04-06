#Round 2
class BankAccount():
    objects_list = []

    def __init__(self,account_name, balance):
        self.name = account_name
        self.balance = balance
        self.objects_list.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self
        else:
            print("You can't take money out during a deposit!")
            return self
        
    def withdraw(self, amount):
        if (amount > 0) and (self.balance >= amount ):
            self.balance -= amount
            return self
        elif amount < 0:
            print("You can't put in money while withdrawing!")
            return self
        elif amount > self.balance:
            print("Not enough funds!")
            return self
        
class User:
    objects_list = {} # created a dict of user objects so we can pull "data" out later using user name

    def __init__(self, user_name):
        self.user_name = user_name
        self.objects_list[user_name] = self
        self.accounts = {} #created an intance of accounts dict with in the user object so we can interact with the bank account by name

    def open_account(self, account_name, balance):
        self.accounts[account_name] = account_name = BankAccount(account_name, balance)
        return self
    
    def give_me_money(self, account_name, amount):
        self.accounts[account_name].withdraw(amount)
        return self

    def take_me_money(self, account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self

    def display_account_balance(self, account_name):
        print(f"{self.user_name}'s {account_name}: ${self.accounts[account_name].balance}")
        return self
        
    @classmethod
    def transfer_money(cls,user_name,type, amount, other_user, other_type):
        if cls.objects_list[user_name].accounts[type].balance >= amount: # a condition to make sure we're not transfering more than we have
            cls.objects_list[user_name].accounts[type].balance -= amount
            cls.objects_list[other_user].accounts[other_type].balance += amount
            print(f"withdrew ${amount} from {str.upper(user_name)} {type} account. {str.upper(user_name)} {type} new Balance: ${cls.objects_list[user_name].accounts[type].balance}")
            print(f"transfered ${amount} to {str.upper(other_user)} {other_type} account. {str.upper(other_user)} {other_type} new Balance: ${cls.objects_list[other_user].accounts[other_type].balance}")
        else:
            print("Not enough funds in the account to transfer!")

#creating new User objects
thien = User("thien")
cam = User("cam")

#calling a user method to open accounts
thien.open_account("checking", 1000)
cam.open_account("checking", 0)
cam.open_account("saving", 250)


print("#The balance of each account when first open")
thien.display_account_balance("checking")
cam.display_account_balance("checking")
cam.display_account_balance("saving")

#calling BankAccount methods to add and subtract from user's balance
print("#The balance after withdraw and deposit methods from User AND BankAccount were called. (Thien withdrew $500 and then deposited $100, while Cam deposited $100)")
#####################################################
thien.give_me_money("checking", 500).take_me_money("checking",100) # give_me_money and take_me_money are withdraw and deposit methods from Class User
cam.accounts["checking"].deposit(100) # deposit is a method from Class BankAccount

thien.display_account_balance("checking")
cam.display_account_balance("checking")


print("#Testing the money transfer method. (Thien took $500 out of his checking account and transfered it over to Cam's saving account)")
##########################################################
thien.transfer_money("thien","checking",500,"cam","saving")





# class BankAccount:

#     def __init__(self, account_name, int_rate = 0, balance = 0):
#         self.account_name = account_name # added a name attribute to make the display of NINJA BONUS more clear
#         self.int_rate = int_rate
#         self.balance = balance

#     def display_info(self):
#         print(f"account name: {self.account_name} \ninterst rate: {self.int_rate} \nbalance: {self.balance} ")
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return self
#         else:
#             print("You can't take money out during a deposit!")
#             return self
        
#     def withdraw(self, amount):
#         if (amount > 0) and (self.balance >= amount ):
#             self.balance -= amount
#             return self
#         elif amount < 0:
#             print("You can't put in money while withdrawing!")
#             return self
#         elif amount > self.balance:
#             print("Not enough funds!")
#             return self
#     def display_account_info(self):
#         print(f"Balance: ${self.balance}")
#         return self
    
#     def yield_interest(self):
#         if self.balance > 0:
#             self.balance += self.balance * self.int_rate
#             print(f"New balance: ${self.balance}")
#             return self
#         else:
#             print("Can't yield interest when the balance is negative!")
#             return self

# class User:
#     users = [] #creating a list for each of the User's account

#     def __init__(self, first_name, last_name, email, age, account_name, int_rate, balance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age =  age
#         self.is_rewards_member = False
#         self.gold_card_points = 0
#         self.accounts = []
#         self.checking_account = BankAccount(account_name, int_rate,  balance)
#         self.accounts.append(self.checking_account)
#         self.users.append(self)


#     def display_info(self):
#         print(f"{self.first_name} \n{self.last_name} \n{self.email} \n{self.age}")


#     def display_accounts(self):
#         for index in self.accounts:
#             print(f"Account name: {index.account_name}, Balance: ${index.balance}, Interst rate: {index.int_rate}")

#     def open_account(self, account_name, int_rate, balance):
#         account_name = BankAccount(str(account_name), int_rate, balance)
#         self.accounts.append(account_name)
#     # @classmethod
#     # def transfer_money(cls, amount, other_user):

# #creating a user 
# thien = User("thien", "Nguyen", "Meowster@meow.com", 28, "checking", 0.01, 1000)
# cam = User("cam", "Nguyen", "Meowster@meow.com", 1, "checking", 0.01, 2000)

# thien.accounts[0].display_info() # to check the balance of thien's checking account
# thien.accounts[0].deposit(20) # deposit $20 into thien's checking account
# thien.accounts[0].display_info() # check the balance of thien's checking is updated
# thien.accounts[0].withdraw(100) # take out $100 from thien's checking account
# thien.accounts[0].display_info()  # to check the balance of thien's checking is updated

# #senpai bonus
# thien.open_account("saving", 0.10, 20) # creating a second bank account for the user Thien, and we're naming it "saving", it has 10% interest and a balance of $20
# thien.accounts[1].display_info() # displaying the saving account's name, balance and interest rate
# thien.accounts[1].deposit(100) # adding $100 to the saving account
# thien.accounts[1].display_info() # displaying the saving account's updated balance, it should be $120 after the $20 deposit
# thien.accounts[1].withdraw(60) # taking out $60 from saving
# thien.accounts[1].display_info()# saving balance should now be $60

# #to check all of thien's bank accounts
# thien.display_accounts() 



