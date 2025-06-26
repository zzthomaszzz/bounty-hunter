from bounty_hunter import *

class Player:
    def __init__(self, bounty_hunter = BountyHunter()):
        self.bounty_hunter = bounty_hunter
        self.current_health = self.bounty_hunter.max_health

if __name__ == "__main__":
    pass