class Realestate:
    def __init__(self, name, value, rent):
        self.name = name
        self.value = value
        self.rent = rent
        self.owner = ""

    def buyIt(self):
        self.owner = "player"
    
