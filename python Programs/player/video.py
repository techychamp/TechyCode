import PIL.Image,PIL.ImageTk
import tkinter as tk
import time
from video_player import Video
class player():
        def __init__(self,src):
                self.window=tk.Tk()
                self.video=Video(src)
                self.canvas=tk.Canvas(self.window,width=self.video.width,height=self.video.height)
                self.canvas.pack()
                tk.Frame(self.window).pack(side="bottom")
                tk.Button(self.window,text="play/pause",command=self.play).pack(side="left")
                self.delay=5
                #int(self.video.prop(cv2.CAP_PROP_FPS))
                self.playing=True
                self.update()
                self.window.mainloop()
        def play(self):
                if self.playing==True:
                        self.playing=False
                else:
                        self.playing=True
                        self.update()
        def update(self):
                if(self.playing!=True):
                        return 1
                else:
                        ret, frame = self.video.retrive()
                        if ret==True:
                                self.photo=PIL.ImageTk.PhotoImage(image=frame)
                                self.canvas.create_image(0,0,image=self.photo,anchor=tk.NW)
                                self.window.after(self.delay,self.update)
                        else:
                                self.playing=False
        
                
mp4=player("4.mp4")
