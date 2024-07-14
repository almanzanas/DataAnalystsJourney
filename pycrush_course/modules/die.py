from random import randint

class Die:
    """Represents a single die"""

    def __init__(self, num_sides=6):
        """six sides default die"""
        self.num_sides = num_sides
    
    def roll(self):
        """Return a random value taking on acount num_sides"""
        return randint(1, self.num_sides)
