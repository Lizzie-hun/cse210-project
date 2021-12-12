from game.actor import Actor
from game.point import Point
from game import constants

class User_input(Actor):
    def __init__(self):
        super().__init__()


        x = int(constants.USER_INPUT_X)
        y = int(constants.USER_INPUT_Y)
        position = Point(x, y)

        dx = int(constants.USER_INPUT_DX)
        dy = int(constants.USER_INPUT_DY)
        velocity = Point(dx,dy)
        
        self.set_height(constants.USER_INPUT_HEIGHT)
        self.set_width(constants.USER_INPUT_WIDTH)
        self.set_position(position)
        self.set_velocity(velocity)

    def add_text(self, text):
        self._text += text
