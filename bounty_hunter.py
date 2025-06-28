
class BountyHunter:

    def __init__(self, attack = 10, defense = 0, max_health = 100, attack_range = 1, move_speed = 1):
        self.name = "Base bounty hunter"
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.attack_range = attack_range
        self.move_speed = move_speed

class Sniper(BountyHunter):
    name = "Sniper"
    def __init__(self):
        super().__init__(attack = 20, defense = 5, max_health = 120, attack_range = 3, move_speed=1)
        self.name = "Sniper"

class Bruiser(BountyHunter):
    name = "Bruiser"
    def __init__(self):
        super().__init__(attack = 17, defense = 8, max_health = 150, attack_range = 1, move_speed=2)
        self.name = "Bruiser"

class Protector(BountyHunter):
    name = "Protector"
    def __init__(self):
        super().__init__(attack = 5, defense = 12, max_health = 180, attack_range = 2, move_speed=2)
        self.name = "Protector"

class Tank(BountyHunter):
    name = "Tank"
    def __init__(self):
        super().__init__(attack = 10, defense = 10, max_health = 240, attack_range = 1, move_speed=1)
        self.name = "Tank"

if __name__ == "__main__":
    pass