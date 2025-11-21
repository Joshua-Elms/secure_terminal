from pynput import keyboard, mouse
import os
from safety_config import (
    use_alternate_shutdown_method,
    mouse_move_message,
    mouse_move_volume,
    mouse_click_message,
    mouse_click_volume,
    shutdown_voice,
    greeting_message,
    greeting_volume,
    greeting_voice
)


def yell(msg, vol, voice):
    os.system(
        f"osascript -e 'set volume output volume {vol * 10}' && say {msg} -v '{voice}'"
    )


def shutdown():
    cmd = "pmset displaysleepnow"
    if use_alternate_shutdown_method:
        cmd = "pmset sleepnow"
    os.system(cmd)



def mouse_tracker(shutdown_on_movement):
    def on_move(x, y):
        if shutdown_on_movement:
            yell(mouse_move_message, mouse_move_volume, shutdown_voice)
            shutdown()
            return False
        else:
            pass

    def on_click(x, y, button, pressed):
        yell(mouse_click_message, mouse_click_volume, shutdown_voice)
        shutdown()
        return False
    
    def on_scroll(x, y, dx, dy):
        pass

    # Collect events until released
    with mouse.Listener(
        on_move=on_move, on_click=on_click, on_scroll=on_scroll
    ) as listener:
        listener.join()


current_input = ""


def keyboard_tracker(secret_code):
    def on_press(key):
        pass

    def on_release(key):
        global current_input
        try:
            current_input += key.char
            if len(current_input) >= len(secret_code):
                if current_input[-len(secret_code) :] == secret_code:
                    print("Secret code entered!")
                    yell(greeting_message, greeting_volume, greeting_voice)
                    return False
        except AttributeError:
            pass
        except TypeError:
            print(f"Shutdown successful")
            pass

    # Collect events until released
    with keyboard.Listener(
        on_press=on_press, on_release=on_release, suppress=True
    ) as listener:
        listener.join()
