class Team:
    def __init__(self, name, slogan):
        self.name = name
        self.slogan = slogan
        
    def show_info(self):
        print(f"Team{self.name} - {self.slogan}")
        
team = Team("Man-U", "Red Devils")
team = Team("Arsenal", "Losers")
