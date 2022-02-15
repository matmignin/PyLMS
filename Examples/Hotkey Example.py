import keyboard



def on_space():
    keyboard.write('The quick brown fox jumps over the lazy dog.')


keyboard.add_hotkey('ctrl+Shift+space', on_space)




keyboard.wait('esc')