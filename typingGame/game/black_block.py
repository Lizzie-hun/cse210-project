from game.actor import Actor
from game.point import Point
from game import constants

class Black_block(Actor):
    def __init__(self):
        super().__init__()
        
        self.x = 0
        self.y = 0

        self.color = constants.BLACK_BLOCK_COLOR
        self.set_width(constants.BLACK_BLOCK_WIDTH)
        self.set_height(constants.BLACK_BLOCK_HEIGHT)

    def create_bricks(self, x, y):
        if x == 0:
            x = constants.BLACK_BLOCK_SPACE * 2
            y = constants.BLACK_BLOCK_SPACE * 2
        elif x < constants.MAX_X:
            if x > constants.MAX_X - constants.BLACK_BLOCK_WIDTH * 2:
                x = constants.BLACK_BLOCK_SPACE * 2
                y = y + constants.BLACK_BLOCK_HEIGHT + constants.BLACK_BLOCK_SPACE
            else:
                x = x + constants.BLACK_BLOCK_WIDTH + constants.BLACK_BLOCK_SPACE

        position = Point(x, y)

        self.set_position(position)
            