players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
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


class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.age = dict['age']
        self.position = dict['position']
        self.team = dict['team']
    @classmethod
    def get_team(cls, team_list):
        new_team = []
    # Create new Player object from list players
        for i in range(len(team_list)):
            player_i = cls(team_list[i])
            new_team.append(player_i)
        return new_team

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Set new variable for team_1 to the returned value of running the players list through the class method get_team
team_1 = Player.get_team(players)

print(team_1[0].age)