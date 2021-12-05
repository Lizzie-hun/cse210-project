from game.actor import Actor
from game.point import Point
from game import constants


class Image(Actor):
    def __init__(self):
        x = constants.BACKGROUND_X
        y = constants.BACKGROUND_Y
        position = Point(x,y)

        velocity = Point(0,0)

        self.set_width(constants.MAX_X)
        self.set_height(constants.MAX_Y)
        self.set_image(constants.BACKGROUND_IMAGE)
        self.set_position(position)
        self.set_velocity(velocity)