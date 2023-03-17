import PIL.Image,PIL.ImageTk,threading
from concurrent.futures import *
import tkinter as tk
import time
from math import ceil,floor
from video_player import Video
from audio_player import Audio
class player():
        def __init__(self,src):
                self.window=tk.Tk()
                #self.window.aspect(300,500,650,750)
                self.video=Video(src)
                self.audio=Audio(src)
                #self.frame=tk.Frame(self.window)
                #self.frame.grid(rows=5)
                self.height=self.video.height
                self.width=self.video.width
                self.audio_len=self.audio.length
                self.canvas=tk.Canvas(self.window,width=self.width,height=self.height)
                self.canvas.pack(anchor="center",fill="x",expand=True)
                self.frame2=tk.Frame(self.window,width=1)
                self.frame2.pack(side="bottom")
                tk.Button(self.frame2,width=10,height=1,text="play/pause",command=self.play).pack(side="left")
                self.volume_bar=tk.Scale(self.frame2,sliderlength=15,showvalue=0,to=100,command=self.volume_c)
                self.volume_bar.pack(side="right")
                self.volume_bar.set(100)
                self.progress_bar=tk.Scale(self.frame2,repeatdelay=100000,showvalue=0,sliderlength=10,length=self.width-30+10,to=self.audio_len,orient=tk.HORIZONTAL,command=self.progress)
                self.progress_bar.pack(side="right")
                self.delay=46
                self.draw_loc=[0,0]
                self.playing=False
                self.player_pause=False
                self.cur_frame=0
                self.cur_audio=0
                self.cur_percent=0
                self.frame_upcnt=(1/self.video.fps)*1000
                self.div_c=lambda :ceil(self.frame_upcnt) if(self.cur_audio%3==0)else floor(self.frame_upcnt)
                self.div=ceil(self.frame_upcnt) if(self.cur_audio%3==0)else floor(self.frame_upcnt)
                self.get_percent=lambda x,y:((x/y)*100)if(x<y)else((y*x)/100)
                self.frame_count=self.video.prop(7)
                self.window.bind("<Destroy>",lambda x:self.des(x))
                self.progress_bar.bind("<Button-1>",lambda x:self.des(x))
                self.progress_bar.bind("<ButtonRelease>",lambda x:self.des(x))
                self.window.bind("<Expose>",lambda x:self.fr_resize())
                self.play()
                self.window.mainloop()
        def des(self,x):
                global t
                if(x.type==tk.EventType.Destroy):
                        self.playing=False
                elif(x.type==tk.EventType.ButtonPress):
                        t=x
                        if(self.playing==True):
                                self.player_pause=True
                        self.playing=False
                elif(x.type==tk.EventType.ButtonRelease):
                        t=x
                        if(self.player_pause==True):
                                self.player_pause=False
                                self.play()
                        else:
                                self.frame_change("")
                                self.vid_play(True)
                                
        def play(self):
                if self.playing==True:
                        self.playing=False
                else:
                        self.update()
        def vid_play(self,play=False):
                if(self.playing==True)or(play==True):
                        ret, frame = self.video.retrive()
                        if ret==True:
                                self.photo=PIL.ImageTk.PhotoImage(image=frame)
                                self.canvas.create_image(self.draw_loc[1],self.draw_loc[0],image=self.photo,anchor=tk.NW)
                                self.cur_frame=(self.cur_frame+1)if(play==False)else(self.cur_frame)
                                self.div=self.div_c()
                                #self.fr_resize()
                                self.progresser()
                                #self.window.after(self.delay,self.vid_play)
                        else:
                                self.playing=False
                        
                else:
                        return 1
        def audio_play(self):
                self.fr_resize()
                self.vid_play(True)
                self.div=ceil(self.frame_upcnt) if(self.cur_audio%3==0)else floor(self.frame_upcnt)
                for i in range(self.cur_audio,self.audio_len):
                        if(self.playing==True):
                                self.audio.play()
                                #self.change()
                                #with ThreadPoolExecutor(max_workers=1) as executor:
                                        #executor.submit()
                                self.cur_percent=self.get_percent(self.cur_audio,self.audio_len)
                                if(self.cur_audio%self.div==0):
                                        self.window.after(self.delay,self.vid_play)
                                #threading.Thread(target=self.change).start()
                                self.cur_audio+=1
                        else:
                                break
        def progresser(self):
                if(self.playing==True):
                        self.progress_bar.set(self.cur_audio)
        def frame_change(self,typ="v"):
                per=lambda x:int(round(self.get_percent(x,self.cur_percent),0))
                if(typ=="v"):
                        self.video.set_frame(per(self.frame_count))
                elif(typ=="a"):
                        self.audio.counter=per(self.audio_len)
                else:
                        self.cur_audio=self.progress_bar.get()
                        self.video.set_frame(per(self.frame_count))
                        self.audio.counter=self.cur_audio
                        #per(self.audio_len)
        def fr_resize(self):
                self.height=self.window.winfo_height()-6*10
                self.width=self.window.winfo_width()-4
                self.height=int(round((self.width*self.video.ratio[0]),0))
                if(self.window.winfo_height()-6*10<self.height):
                        self.width=int(round((self.window.winfo_height()-6*10)*self.video.ratio[1],0))
                        self.height=int(round(((self.width)*self.video.ratio[0]),0))
                self.width,self.height=self.video.resolution(self.width,self.height)
                self.draw_loc=[((self.window.winfo_height()-6*10)-self.height)/2,((self.window.winfo_width())-self.width)/2]
                self.canvas.config(height=self.window.winfo_height()-6*10,background="#0b0b0b")
                if self.playing==False:
                        self.video.set_frame(self.cur_frame)
                        self.vid_play(True)
        def change(self):
                pass
                
        def progress(self,t):
                self.cur_percent=self.get_percent(int(t),self.audio_len)
        def volume_c(self,v):
                self.audio.volume=int(v)
        def update(self):
                if(self.playing!=True):
                        self.playing=True
                        self.frame_change("")
                        t2=threading.Thread(target=self.audio_play)
                        t2.start()
                        t1=threading.Thread(target=self.vid_play)
                        t1.start()
        
#mp4=player("c:/users/karuna/music/en kaadhal nee.mp4")
mp4=player("video_1.mp4")

