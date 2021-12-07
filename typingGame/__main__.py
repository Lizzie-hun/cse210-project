import os
#os.environ['RAYLIB_BIN_PATH'] = '.'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.black_block import Black_block
from game.story import Story
from game.user_input import User_input
from game.image import Image
from game.text_background import Text_background
from game.control_actors_action import ControlActorsAction
from game.handle_edge_bounce import HandleEdgeBounce
from game.handle_adding_letter import HandleAddingLetter
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    image = Image()
    cast["image"] = [image]


    black_blocks = []
    
    x = 0
    y = 0

    for n in range(constants.BLACK_BLOCK_ROWS * constants.BLACK_BLOCK_COLUMNS):
        black_block = Black_block()
        black_block.create_bricks(x,y)
        black_blocks.append(black_block)
        position = black_block.get_position()
        x = position.get_x()
        y = position.get_y()

    cast["black_block"] = black_blocks


    text_background  = Text_background()
    cast["text_background"] = [text_background]

    story = Story()
    cast["story"] = [story]
    # TODO: Create a ball here and add it to the list

    user_input = User_input()
    cast["user_input"] = [user_input]
    # TODO: Create a paddle here and add it to the list

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_edge_bounce = HandleEdgeBounce(physics_service)
    handle_adding_letter = HandleAddingLetter(input_service)
    control_actors_action = ControlActorsAction(input_service)

    # TODO: Create additional actions here and add them to the script
    script["input"] =  [handle_adding_letter]
    script["update"] = [move_actors_action, handle_edge_bounce, control_actors_action]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Typing Game");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    if black_blocks:
        continue_game = True
    else:
        continue_game = False
    #if continue_game == False:
        #audio_service.play_sound(constants.SOUND_OVER)
    audio_service.stop_audio()
   
        

if __name__ == "__main__":
    main()