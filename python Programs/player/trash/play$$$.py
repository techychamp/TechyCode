import PIL.Image,PIL.ImageTk,threading
import tkinter as tk
import time
from math import ceil,floor
from video_player import Video
from audio_player import Audio
class Ui(tk.Tk):
        def __init__(self,vals,functions):
                super().__init__(None)
                self.vals=vals
                self.video=Video(vals[1])
                self.get_percent=lambda x,y:((x/y)*100)if(x<y)else((y*x)/100)
                #super.__init__()
                self.cur_percent=vals[2]
                self.playing=vals[3]
                self.draw_loc=[0,0]
                self.cur_frame=0
                self.frame_upcnt=(1/self.video.fps)*1000
                self.height=self.video.height
                self.width=self.video.width
                self.canvas=tk.Canvas(height=self.height,width=self.width)
                self.canvas.pack(anchor="center",fill="x",expand=True)
                self.frame2=tk.Frame(width=1)
                self.frame2.pack(side="bottom")
                tk.Button(width=10,height=1,text="play/pause",command=functions[0]).pack(side="left")
                self.volume_bar=tk.Scale(sliderlength=15,showvalue=0,to=100,command=functions[1])
                self.volume_bar.pack(side="right")
                self.volume_bar.set(50)
                self.progress_bar=tk.Scale(repeatdelay=100000,showvalue=0,sliderlength=10,orient=tk.HORIZONTAL,length=self.width-30+10,to=vals[0],command=self.progress)
                self.progress_bar.pack(side="right")
        def vid_play(self,play=False):
                ret, frame = self.video.retrive()
                if ret==True:
                        self.phto=PIL.ImageTk.PhotoImage(image=frame)
                        self.canvas.create_image(self.draw_loc[1],self.draw_loc[0],image=self.phto,anchor=tk.NW)
                        self.cur_frame=(self.cur_frame+1)if(play==False)else(self.cur_frame)
                        return 1
                else:
                        return 0
        def fr_resize(self):
                self.height=self.winfo_height()-6*10
                self.width=self.winfo_width()-4
                self.height=int(round((self.width*self.video.ratio[0]),0))
                if(self.winfo_height()-6*10<self.height):
                        self.width=int(round((self.winfo_height()-6*10)*self.video.ratio[1],0))
                        self.height=int(round(((self.width)*self.video.ratio[0]),0))
                self.width,self.height=self.video.resolution(self.width,self.height)
                self.draw_loc=[((self.winfo_height()-6*10)-self.height)/2,((self.winfo_width())-self.width)/2]
                self.canvas.config(height=self.winfo_height()-6*10,background="#0b0b0b")
                self.video.set_frame(self.cur_frame)
                self.vid_play(True)
        def progress(self,t):
                if(self.playing[0]==True):
                        self.cur_percent[0]=self.get_percent(int(t),self.vals[0])
class Controls():
        def __init__(self,src):
                self.audio=Audio(src)
                self.delay=500#46
                self.audio_len=self.audio.length
                self.playing=[False]
                self.player_pause=False
                self.cur_audio=0
                self.cur_percent=[0]
                self.window=Ui((self.audio_len,src,self.cur_percent,self.playing),(self.play,self.volume_c))
                self.cur_upcnt=self.window.frame_upcnt
                self.get_percent=lambda x,y:((x/y)*100)if(x<y)else((y*x)/100)
                self.frame_count=self.window.video.prop(7)
                self.window.bind("<Destroy>",self.des)
                self.window.progress_bar.bind("<Button-1>",self.des)
                self.window.progress_bar.bind("<ButtonRelease>",self.des)
                self.window.bind("<Expose>",lambda x:self.window.fr_resize())
                self.play()
                self.window.mainloop()
        def des(self,x):
                global t
                if(x.type==tk.EventType.Destroy):
                        self.playing[0]=False
                elif(x.type==tk.EventType.ButtonPress):
                        t=x
                        if(self.playing[0]==True):
                                self.player_pause=True
                        self.playing[0]=False
                elif(x.type==tk.EventType.ButtonRelease):
                        t=x
                        if(self.player_pause==True):
                                self.player_pause=False
                                self.play()
                        else:
                                self.frame_change("")
                                self.vid_play(True)
        def play(self):
                if self.playing[0]==True:
                        self.playing[0]=False
                else:
                        self.update()
        def vid_play(self,play=False):
                if(self.playing[0]==True)or(play==True):
                        if(self.window.vid_play(play)==1):
                                self.progresser()
                                self.cur_upcnt+=self.window.frame_upcnt
                                #self.window.after(self.delay,self.vid_play)
                        else:
                                self.playing[0]=False
                else:
                        return 1
        def progresser(self):
                self.window.progress_bar.set(self.cur_audio)
        def audio_play(self):
                self.window.fr_resize()
                self.vid_play(True)
                for i in range(self.cur_audio,self.audio_len):
                        if(self.playing[0]==True):
                                self.audio.play()
                                self.cur_percent[0]=self.get_percent(self.cur_audio,self.audio_len)
                                if(self.cur_audio%int(self.window.frame_upcnt)==0):
                                        threading.Thread(target=lambda:self.window.after(self.delay,self.vid_play)).start()
                                self.cur_audio+=1
                        else:
                                break
        def frame_change(self,typ="v"):
                per=lambda x:int(round(self.get_percent(x,self.cur_percent[0]),0))
                if(typ=="v"):
                        self.window.video.set_frame(per(self.frame_count))
                elif(typ=="a"):
                        self.audio.counter=per(self.audio_len)
                else:
                        self.cur_audio=self.window.progress_bar.get()
                        self.window.video.set_frame(per(self.frame_count))
                        self.audio.counter=self.cur_audio
                        #per(self.audio_len)
        def volume_c(self,v):
                self.audio.volume=int(v)
        def update(self):
                if(self.playing[0]!=True):
                        self.playing[0]=True
                        self.frame_change("")
                        t2=threading.Thread(target=self.audio_play)
                        t2.start()
                        t1=threading.Thread(target=self.vid_play)
                        t1.start()
        
                                
        
mp4=Controls("c:/users/karuna/music/en kaadhal nee.mp4")
