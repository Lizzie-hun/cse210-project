from game import constants
from game.action import Action
from game.point import Point
from game import audio_service

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

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
        mistake = False
        if text not in story_text.lower():
            mistake = True
        if mistake:
            mistake = False
            black_block.pop(-1)
            #audio_service.play_sound(constants.SOUND_BOUNCE)