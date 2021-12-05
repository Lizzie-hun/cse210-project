from game.actor import Actor
from game.point import Point
from game import constants


class Text_background(Actor):
    def __init__(self):
        super().__init__()

        x = int(constants.STORY_X )
        y = int(constants.STORY_Y)
        position = Point(x, y)

        if x > 0:
            dx = constants.STORY_DX
            dy = constants.STORY_DY
        elif x < 0:
            dx = 0
            dy = 0
        velocity = Point(dx, dy)

        self.color = constants.TEXT_BACKGROUND
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_width(constants.MAX_X)
        self.set_height(constants.STORY_HEIGHT + constants.USER_INPUT_HEIGHT)
        