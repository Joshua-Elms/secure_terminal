from dtom import *
from time import sleep
import pyautogui as pg

for _ in range(shutdown_after_rounds):
    os.system(f"osascript -e 'set volume output volume {volume_level * 10}'")
    say(warning_msg_1, voice)
    say(warning_msg_2, voice)
    sleep(0.5)

if lock_computer:
    pg.hold("a")
    pg.hold("command")
    pg.hold("control")
    pg.hold("q")
