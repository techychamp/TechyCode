import cv2,PIL.Image
class Video():
        def __init__(self,url):
                self.load(url)
                self.width=self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
                self.height=self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
                self.frame_width=self.width
                self.frame_height=self.width
                self.ratio=[self.height/self.width,self.width/self.height]
                self.fps=self.prop(cv2.CAP_PROP_FPS)
        def load(self,url):
                cap = cv2.VideoCapture(url)
                if (cap.isOpened()== False): 
                        print("Error opening video file")
                else:
                        self.video=cap
        def retrive(self):
                ret,frame=self.video.read()
                if(ret==True):
                        return (True,PIL.Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)).resize((int(self.frame_width),int(self.frame_height))))
                else:
                        return (False,None)
        def __del__(self):
                print("video")
                if slef.video.isOpened():
                        self.video.release()
        def prop(self,prp):
                return self.video.get(prp)
        def resolution(self,width=0,height=0):
                if(self.width<=width):
                        self.frame_width,self.frame_height=(width,height)#self.
                else:
                        self.frame_width,self.frame_height=(width,height)
                return self.frame_width,self.frame_height
        def set_frame(self,frame:int):
                self.video.set(cv2.CAP_PROP_POS_FRAMES,frame)
                
