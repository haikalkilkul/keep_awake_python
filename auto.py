"""
This script is created to print time every 10 seconds
The initial plan is to keep laptop screen awake because the sleep option cannot be configured
"""

import keyboard
import time

print("Script started")
print("Press CTRL+ALT+= to toggle")

def press_space():
    keyboard.press_and_release('space')
    
def type_current_time():
    current_time = time.strftime("%H:%M:%S")
    keyboard.write(current_time + '\n')
    
interval = 10
toggle_key = 'ctrl+alt+='

running = False

def toggle():
    global running
    if running:
        print("Status: Stopped")
    else:
        print("Status: Running")
    running = not running

keyboard.add_hotkey(toggle_key, toggle)

while True:
    if running:
        #press_space()
        type_current_time()
    time.sleep(interval)