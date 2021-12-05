from game.actor import Actor
from game.point import Point
from game import constants

class Story(Actor):
    def __init__(self):
        super().__init__()

        x = int(constants.STORY_X)
        y = int(constants.STORY_Y)
        position = Point(x, y)

        dx = constants.STORY_DX
        dy = constants.STORY_DY
        velocity = Point(dx, dy)
        #constants.STORY.append(constants.LIBRARY)
        #for line in constants.LIBRARY:
        #    constants.STORY.append(line)
        #self.set_image(constants.IMAGE_BALL)
        self.set_text(constants.LIBRARY)
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_width(constants.STORY_WIDTH)
        self.set_height(constants.STORY_HEIGHT)
        
