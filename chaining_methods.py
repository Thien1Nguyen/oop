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
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
        
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
            print(f"User have {self.gold_card_points} points left" )
            return self
        else:
            print("User does not have enough points!")
            return self

user_thien = User("Thien","Nguyen","Meowster@meow.com", 29)
user_cam = User("Cam","Nguyen","stinker@meow.com", 1)
user_loafie = User("Loafie","Nguyen","chaser@meow.com", 1)
user_thien.display_info().enroll().spend_points(50).display_info().enroll() # to test if the user is already enroll
user_cam.display_info().spend_points(80)
user_loafie.display_info().spend_points(40)
