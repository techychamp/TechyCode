import urllib.request,ssl,os.path
class web_sock():
    def __init__(self,url):
        self.url=url
        self.headers={
            "Accept-Encoding":"identity;q=1, *;q=0",
            "Range":"bytes=0-",
            "Sec-Fetch-Mode":"no-cors",
            "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
            #"Platform":" Win32"#"Referer":" ",
            }
        self.request=urllib.request.Request(self.url,headers=self.headers,unverifiable=True)#urllib.request.URLopener(context=ssl._create_unverified_context())
        
        self.set_headers()
        self.download()
    def set_headers(self,**args):
        if(args):
            self.headers.update(args)
        map(lambda x:self.request.add_header(x,self.headers[x]),self.headers.keys())
        return 1
    def grab(self):
        #progress(local)
        return urllib.request.urlopen(self.request,timeout=5)
    def download(self,location=""):
        pth=os.path.abspath(location)+"\\"+self.url.rsplit("/",1)[1]
        print(pth)
        f=open(pth,"wb")
        f.write(self.grab().read())
        f.close()
            
grab=web_sock("http://localhost/m3u8/hindhi/18/index.m3u8")

