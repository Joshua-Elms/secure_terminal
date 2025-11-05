import os
import pyautogui as pg
import subprocess
from time import sleep

# no need to modify these
username = os.environ.get("USER")
DISARM = "disarm"
say = lambda msg, voice: os.system(f"say {msg} -v '{voice}'")

# modifiable params
cmd_prompt_msg = (
    f"Hello, {username}. This is a secure system. Please enter your command: "
)
warning_msg_1 = "WARNING! Unauthorized access detected! Initiating lockdown procedure!"
warning_msg_2 = "Weeeeeeeoooooooooooo! Weeeeeeeoooooooooooo!"
voice = (
    "Samantha"  # voice for macOS 'say' command, find more with "say -v ? | grep en_US"
)
shutdown_after_rounds = 1
volume_level = 10  # macOS volume level (0-10)

# main code
print(cmd_prompt_msg)
input_cmd = input()

if input_cmd.lower() == DISARM:
    print("System disarmed. Have a nice day!")

else:
    subprocess.Popen(["python3", "mouse_jiggler.py"])
    shutdown_counter = shutdown_after_rounds
    while shutdown_counter > 0:
        try:
            os.system(f"osascript -e 'set volume output volume {volume_level * 10}'")
            say(warning_msg_1, voice)
            say(warning_msg_2, voice)
            shutdown_counter -= 1
            if shutdown_counter == shutdown_after_rounds - 1:
                sleep(5)  # make it seem like it's done
            else:
                sleep(0.5)
        except KeyboardInterrupt:
            print("Cannot be interrupted! System lockdown in progress!")

    pg.hotkey("command", "ctrl", "q", interval=0.25)
