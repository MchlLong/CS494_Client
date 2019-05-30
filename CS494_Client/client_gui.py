# Michael Long, Gennadii Sytov -- CS494 -- Client Main -- May 2019

from tkinter import *

class gui_controller():

    # Paramaters to control the window
    current_frame = 0 
    width = 640
    height = 480
    screen_width = 0
    screen_height = 0
    
    def __init__(self):
        self.draw_frame()
        pass
        
    def draw_frame(self):

        print("Drawing Frame")
        frame = Tk()
        self.screen_width = frame.winfo_screenwidth()
        self.screen_height = frame.winfo_screenheight()
        print(self.screen_width, ' x ', self.screen_height)
        frame.title = 'CS494 -- Client Application'
        frame.geometry('0x0+0+0')
        frame.geometry("640x480+{}+{}".format( int((self.screen_width-self.width)/2), int((self.screen_height-self.height)/2)))
        mainloop()

        # Draw Login / Connect to Host
        if self.current_frame == 0:
            pass

        # Draw Main Screen
        if self.current_frame == 1:
            pass

