import urllib.request
import os
import file
url="https://hses1.akamaized.net/videos/bharat/rakrsb/329_c6ec98081e/1000244148/1571298106477/cb9dd12abf1f37ca9a31efaca2007311/media-3/"
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
def progress(local):
    #print('Downloading...',int((cu/target)*100),sep=" ",end='\r',flush=True)
    print("downloading",local,sep=" ",end='\n',flush=True)
def grab(local):
    progress(local)
    return urllib.request.urlretrieve(url+local,local)
def recu(cu,target):
    if(cu<=target):
        if(grab('segment-'+str(cu)+'.ts')!=None):
            return recu(cu+1,target)
        else:
            return recu(cu,target)
    else:
        return 1
def miss(arr,index=1):
    if(index<len(arr)):
        if(grab('segment-'+str(arr[index])+'.ts')!=None):
            return miss(arr,index+1)
        else:
            return miss(arr,index)
    else:
        return 1
    
if('index.m3u8' in os.listdir()):
    f=open('index.m3u8','r')
    text=f.readlines()
    f.close()
    text=text[len(text)-2]
    miss(file.file_name_check(['segment-','ts'],os.listdir('.'),0,int((text.rsplit('-',1)[1]).split('.')[0])))
else:
    grab('index.m3u8')
    f=open('index.m3u8','r')
    text=f.readlines()
    f.close()
    text=text[len(text)-2]
    print(int((text.rsplit('-',1)[1]).split('.')[0]))
    recu(0,int((text.rsplit('-',1)[1]).split('.')[0]))
