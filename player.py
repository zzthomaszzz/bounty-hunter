from bounty_hunter import *

class Player:
    def __init__(self, bounty_hunter, _id):
        self.id = _id
        self.bounty_hunter = bounty_hunter
        self.current_health = self.bounty_hunter.max_health

if __name__ == "__main__":
    pass