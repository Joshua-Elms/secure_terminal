import pyautogui as pg
from time import sleep
import random

pg.FAILSAFE = False
while True:
    try:
        x_move = random.randint(-300, 300)
        y_move = random.randint(-150, 150)
        pg.moveRel(x_move, y_move, duration=0.02)
        sleep(0.02)  # wait for 1 second before next move
    except KeyboardInterrupt:
        # this is dangerous cuz it means the jiggler can't be stopped easily
        # but you can always run "pgrep -lf python" and kill the process manually if it gets too jiggly
        print("You can't stop me that easily!")
