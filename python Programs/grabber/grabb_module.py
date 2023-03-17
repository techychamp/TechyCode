import urllib.request
import os
import file,ssl

class grab:
    def __init__(self,url):
        self.url=url
        self.request=urllib.request.URLopener(context=ssl._create_unverified_context())
        self.arr=self.classify()
    def classify(self):
        if('index.m3u8' not in os.listdir()):
            self.curnt_file='index.m3u8'
            self.grab()
        f=open('index.m3u8','r')
        self.count=int(((f.readlines()[len(text)-2]).split('-')[1]).split('.')[0])
        f.close()
        return file.file_name_check(['segment-','ts'],os.listdir('.'),0,self.count)
    def grab(self):
        self.progress()
        return self.request.retrieve(url+self.curnt_file,self.curnt_file)
    
    def retrive(self):
        self.recu(self.arr)
        
    def recu(self,index=0):
        if(index<len(self.arr)):
            self.curnt_file='segment-'+str(self.arr[index])+'.ts'
            if(self.grab()!=None):
                return self.recu(index+1)
            else:
                return self.recu(index)
        else:
            return 1
        
    def progress(self):
        print("downloading",self.curnt_file,sep=" ",end='\n',flush=True)
url="https://hses1.akamaized.net/videos/bharat/rakrsb/308_5f44f326b6/1000243126/1569272617004/df2c60faf93480c49431bbd2bc914977/media-3/"
grab(url)
