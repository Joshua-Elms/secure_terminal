import pyautogui as pg
from time import sleep
import random

pg.FAILSAFE = False
while True:
    x_move = random.randint(-300, 300)
    y_move = random.randint(-150, 150)
    pg.moveRel(x_move, y_move, duration=0.02)
    sleep(0.02)  # wait for 1 second before next move
