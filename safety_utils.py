from pynput import keyboard, mouse
from time import sleep
import os


def yell(msg, vol=7):
    os.system(
        f"osascript -e 'set volume output volume {vol * 10}' && say {msg} -v 'Samantha'"
    )


def shutdown():
    os.system("pmset displaysleepnow")



def mouse_tracker(shutdown_on_movement):
    def on_move(x, y):
        if shutdown_on_movement:
            yell("Mouse moved. Initiating shutdown.")
            shutdown()
            return False
        else:
            pass

    def on_click(x, y, button, pressed):
        yell("Mouse clicked. Initiating shutdown.")
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
                    yell("Welcome, Josh.", vol=5)
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
