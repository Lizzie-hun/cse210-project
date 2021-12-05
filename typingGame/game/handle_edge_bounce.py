import random
from game.move_actors_action import MoveActorsAction
from game import constants
from game.action import Action
from game.audio_service import AudioService
from game.point import Point

class HandleEdgeBounce(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._move_actors_action = MoveActorsAction()

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()

        text_background = cast["text_background"][0]

        position = text_background.get_position()
        x = position.get_x()

        if x < 0:
            dx = 0
            dy = 0
        
            velocity = Point(dx, dy)

            text_background.set_velocity(velocity)