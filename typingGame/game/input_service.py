import sys
from game.point import Point
import pyray

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass


    def window_should_close(self):
        """Determines if the user is trying to close the window

        Args:
            self (InputService): An instance of InputService.
        """
        return pyray.window_should_close()
        
    def get_letter(self):
        """Collects the user input into a string.

        Args:
            self (InputService): An instance of InputService.
        
        """
        key_string = ""
        key_int = pyray.get_key_pressed()
        if key_int != -1:
            key_string = chr(key_int)
        return key_string
