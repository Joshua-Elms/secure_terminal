import os
import subprocess

# no need to modify these
username = os.environ.get("USER")
DISARM = "disarm"
say = lambda msg, voice: os.system(f"say {msg} -v '{voice}'")

# modifiable params
cmd_prompt_msg = f"(base) {username}$ "
warning_msg_1 = "Ahhhhh Paul is trying to attack Joshs computer! Someone please help!"
warning_msg_2 = "Grrr"
voice = "Samantha"
lock_computer = True  # set to False to skip locking the computer
shutdown_after_rounds = 3
volume_level = 7  # macOS volume level (0-10)


if __name__ == "__main__":
    # main code
    input_cmd = input(cmd_prompt_msg)

    if input_cmd.lower() == DISARM:
        print("System disarmed. Have a nice day!")

    else:
        subprocess.Popen(["python3", "mouse_jiggler.py"])
        subprocess.Popen(["python3", "countdown.py"])
