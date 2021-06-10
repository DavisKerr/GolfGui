from View.double_slider import Double_Slider
from tkinter import *
from PIL import ImageTk, Image
from tkvideo import tkvideo
from tkinter import filedialog

class Analysis_Screen(filename):

    def __init__(self, slider_function):
        self.window = Tk()
        self.window.title("Golf Analyzer")
        self.window.iconbitmap("Images/Golf.ico")
        self.slider_function = slider_function

        self.build_window()

        self.window.mainloop()
    
    def load_video(self):
        self.video_player = tkvideo(self.filename, self.video_display, loop=1, size=(400,400))
        self.video_player.play()


    def build_window(self):
        self.title = Label(self.window, text="Record and trim golf stroke video")
        
        self.video_display = Label(self.window)
 
        self.play_btn = Button(self.window, text="Play")
        self.pause_btn = Button(self.window, text="Pause")
        self.record_btn = Button(self.window, text="Record")
        self.video_slider = Double_Slider(self.window, lambda x : x)
        self.submit_btn = Button(self.window, text="Submit Selection")
        self.btnView = Button(self.window, text="View")
        self.readout = Text(self.window)

        self.btnView.grid(row=0, column=0)
        self.title.grid(row=1, column=3)
        self.video_display.grid(row=1, column=1, rowspan=3, columnspan=5)
        self.play_btn.grid(row=6, column=2)
        self.pause_btn.grid(row=6, column=3)
        self.record_btn.grid(row=6, column=4)
        self.video_slider.grid(row=7, column=1, columnspan=5)
        self.submit_btn.grid(row=8, column=3)
        self.readout.grid(row=9, column=1, columnspan=5)

