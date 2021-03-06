import pyray
from game import constants
from game.action import Action
from game.point import Point
from game.output_service import OutputService

class ControlActorsAction(Action):
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
        user_input = cast["user_input"][0]
        story = cast["story"][0]
        story_text = story.get_text()
        text = user_input.get_text()

        if len(text) > 0:
            index = len(text)-1
            if text[index] != story_text[index]:
                replace = story_text[:index]
                text = replace
                user_input.set_text(text)
                for i in range(16):
                    black_block.pop(-1)
                    self._audio_service.play_sound(constants.SOUND_BOUNCE)
