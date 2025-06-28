from bounty_hunter import *

class Player:
    def __init__(self, bounty_hunter, _id):
        self.id = _id
        self.bounty_hunter = bounty_hunter
        self.current_health = self.bounty_hunter.max_health
        self.position = [0, 0]
        self.team_id = 0

    def get_position(self):
        return self.position

    def set_team(self, number):
        self.team_id = number

if __name__ == "__main__":
    pass