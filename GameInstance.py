from classes.Player import *
from classes.Community import *

class GameInstance:
    """Game instance """

    def __init__(self, startDate):
        self.date = startDate

        self.player = PlayerClass(0, 0, 0, 0, 0, 0)
        self.economy = Economy(0, 0, 0)

