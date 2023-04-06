"""
For this assignment you will create the user class and add a couple methods!

Attributes:
On instantiation of a user, the following attributes should be passed in as arguments:

first_name
last_name
email
age
Also include default attributes:

is_rewards_member - default value of False
gold_card_points = 0
Methods:
display_info(self) - Have this method print all of the users' details on separate lines.
enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
spend_points(self, amount) - have this method decrease the user's points by the amount specified.
Ninja Bonuses:

Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
"""
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age =  age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name} \n{self.last_name} \n{self.email} \n{self.age}")

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
        
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
            print(f"User have {self.gold_card_points} points left" )
            return self.gold_card_points
        else:
            print("User does not have enough points!")

user_thien = User("Thien","Nguyen","Meowster@meow.com", 29)
user_thien.display_info()
user_thien.enroll()
user_cam = User("Cam","Nguyen","stinker@meow.com", 1)
user_loafie = User("Loafie","Nguyen","chaser@meow.com", 1)
user_thien.spend_points(50)
user_cam.enroll()
user_cam.spend_points(80)
user_thien.display_info()
user_cam.display_info()
user_loafie.display_info()
user_thien.enroll() # to test if the user is already enroll
user_loafie.spend_points(40)

