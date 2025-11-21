from time import sleep
import subprocess
from safety_config import buffer_time

# give user time to switch to another window
for i in range(buffer_time, 0, -1):
    print(f"Securing system in {i} seconds...", end="\r")
    sleep(1)
print("System secured." + " " * 30)  # clear line
    
mouse_script = subprocess.Popen(["python3", "mouse_script.py"])
keyboard_script = subprocess.Popen(["python3", "keyboard_script.py"])

while keyboard_script.poll() is None:
    if mouse_script.poll() is not None:
        keyboard_script.terminate()
    sleep(1)
    
mouse_script.terminate()
print("System restored.")