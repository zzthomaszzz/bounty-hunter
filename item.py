
class Item:
    def __init__(self, price = 10):
        self.name = "Base Item"
        self.price = price

class BroadSword(Item):
    def __init__(self):
        super().__init__(price = 50)
        self.name = "Broad sword"


if __name__ == "__main__":
    pass