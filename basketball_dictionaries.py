players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]




#creating a Player class
class Player:
    players =[]
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]
        self.players.append(self)

    def display_player_info(self):
        print(f"player name:{self.name}, player age: {self.age}, player position: {self.position}, player play for the: {self.team}")
    @classmethod
    def all_players_display(cls):
        for player in cls.players:
            print(f"{player.name}, {player.age}, {player.position}, {player.team}")




kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_kevin = Player(kevin)
player_kevin.display_player_info()
player_jason = Player(jason)
player_jason.display_player_info()
player_kyrie = Player(kyrie)
player_kyrie.display_player_info()

#creating players from the given players list
new_team = {}

#a function to convert players list into a dictionary of player objects
def player_api_to_list(api):
    for index in api: #looping throught the players list and adding new player objects into the new_team dictionary
        # print(new_team)
        new_team[index['name']] = Player(index)
        


#calling the function
player_api_to_list(players)

#calling the class method to check on all of the player objects
Player.all_players_display()

