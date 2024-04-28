### Creating the RandomWalk Class
# It will need three attributes. One to track number of points in the walk, 
# and two lists to store de x and y coords.

from random import choice # choice() function will make move decisions

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000): # Default number of points
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_val = [0]
        self.y_val = [0]

    ### Choosing Directions
    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches 'num_points'
        while len(self.x_val) < self.num_points:

            # Decide which direction to go, and how far to go (right or left, up or down, and how far)
            x_direction = choice([1, -1]) # 1 = right; -1 = left
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance # positive move up, negative move down

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            y = self.y_val[-1] + y_step
            x = self.x_val[-1] + x_step

            self.x_val.append(x)
            self.y_val.append(y)
            