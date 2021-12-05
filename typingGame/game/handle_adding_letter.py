import random
from game import constants
from game.action import Action


class HandleAddingLetter(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, input_service):
        super().__init__()
        self._input_service = input_service
        
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        user_input = cast["user_input"][0]
        letter = self._input_service.get_letter()
        if letter != "":    
            user_input.set_text(letter)