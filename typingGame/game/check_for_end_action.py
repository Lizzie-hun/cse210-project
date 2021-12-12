import pyray
from game import constants
from game.action import Action

class CheckForEndAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, audio_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._audio_service = audio_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        black_block = cast["black_block"]

        if not black_block:
            self._audio_service.stop_audio()
            pyray.close_window()
            print("Game over!")

        if constants.STORY == constants.USER_INPUT:
            self._audio_service.stop_audio()
            pyray.close_window()
            print("You won!")