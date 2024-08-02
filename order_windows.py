import pygetwindow as gw
from pywinauto import Desktop
import screeninfo as si

#! This should have been a script to move opened windows to specific monitors, but I gave up on figuring out how it's decided wich display gets priority.
#?However this is pretty functional, apart the fact that the + 1920 at line 31 launches the tab somewhere into stratosphere

def get_relevant_windows():# Get the list of all open windows
    windows = Desktop(backend="uia").windows()
    print(windows)
    for window in windows:
        text_wrap = window.window_text()
        
        if 'Глава' in text_wrap or 'глава' in text_wrap:
            ch_folder = text_wrap
            print(ch_folder)
        elif 'Hinamatsuri' in text_wrap:
            ch_tab = text_wrap
            print(ch_tab)
    return ch_folder, ch_tab

def move_windows(windows):
    screens = si.get_monitors()
    for screen in screens:
        print(screen)
        if 'is_primary=False' in str(screen):
            second_monitor = screen

    for window in windows:
        moving_window = Desktop().window(title=window)
        moving_window.move_window(second_monitor.x + 1920)



windows = get_relevant_windows()
move_windows(windows)