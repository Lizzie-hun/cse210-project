import os

import pyray

MAX_X = 1200
MAX_Y = 800
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

BACKGROUND_IMAGE = os.path.join(os.getcwd(),"./typingGame/assets/background.png")
IMAGE_BRICK = os.path.join(os.getcwd(), "./typingGame/assets/brick-6.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./typingGame/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./typingGame/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./typingGame/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./typingGame/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./typingGame/assets/over.wav")

BACKGROUND_X = 0
BACKGROUND_Y = 0

STORY_X = MAX_X - 5
STORY_Y = MAX_Y - 250

STORY_DX = -2
STORY_DY = 0

BLACK_BLOCK_ROWS = int(32)
BLACK_BLOCK_COLUMNS = int(48)

USER_INPUT_X = STORY_X
USER_INPUT_Y = STORY_Y + DEFAULT_FONT_SIZE + 5

BLACK_BLOCK_WIDTH = 24
BLACK_BLOCK_HEIGHT = 24

BLACK_BLOCK_SPACE = 1

USER_INPUT_DX = STORY_DX
USER_INPUT_DY = STORY_DY

USER_INPUT_WIDTH = 96
USER_INPUT_HEIGHT = 24

STORY_WIDTH = 24
STORY_HEIGHT = 24

BLACK_BLOCK_COLOR = pyray.BLACK
TEXT_BACKGROUND = pyray.WHITE

PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/paragraph1.txt").read().lower()
STORY = []

USER_INPUT = ""