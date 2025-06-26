
class BountyHunter:

    def __init__(self, attack = 10, defense = 0, max_health = 100, attack_range = 1, move_speed = 2):
        self.name = "Base bounty hunter"
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.attack_range = attack_range
        self.move_speed = move_speed

class Sniper(BountyHunter):

    def __init__(self):
        super().__init__(attack = 35, defense = 15, max_health = 150, attack_range = 5, move_speed = 2)
        self.name = "Sniper"

class Bruiser(BountyHunter):

    def __init__(self):
        super().__init__(attack = 45, defense = 30, max_health = 400, attack_range = 1, move_speed = 2)
        self.name = "Bruiser"

class Protector(BountyHunter):

    def __init__(self):
        super().__init__(attack = 20, defense = 20, max_health = 300, attack_range = 2, move_speed = 3)
        self.name = "Protector"

class Tank(BountyHunter):

    def __init__(self):
        super().__init__(attack = 25, defense = 50, max_health = 500, attack_range = 1, move_speed = 1)
        self.name = "Tank"

if __name__ == "__main__":
    pass