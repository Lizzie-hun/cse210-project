import os

MAX_X = 1200
MAX_Y = 800
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICK = os.path.join(os.getcwd(), "./batter/assets/brick-6.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

STORY_X = MAX_X
STORY_Y = MAX_Y - 125

STORY_DX = 8
STORY_DY = 0

BRICK_ROWS = int(7)
BRICK_COLUMNS = int(15)

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

PADDLE_SPEED = 10

PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

STORY_WIDTH = 24
STORY_HEIGHT = 24