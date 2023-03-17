import socket
from time import sleep
class server(socket.socket):
    def __init__(self):
        super().__init__()
        self.bind(("",1234))
        self.listen(1)
        self.client,self.addr=self.accept()
        self.cluster=10000
        print(self.addr)
    def readfile(self,url):
        file=open(url,"rb")
        self.data=file.read()
        count=len(self.data)/self.cluster
        flag=int(str(count).split(".")[1])
        self.count=int(count)
        if(flag!=0):
            self.count+=1
    def send_dta(self,cnt):
        if cnt==self.count :
            dta=self.data[self.count*self.cluster::]
        else:
            dta=self.data[cnt*self.cluster:(cnt+1)*self.cluster]
        self.client.send(dta)
        if(1):
            return 1
        else:
            print("error")
            return 0
    def send_file(self,url):
        print("sending",url)
        self.readfile(url)
        self.client.send(bytes(str(tuple([url.split("/",1)[-1],self.count,(10)if(self.count!=1)else(1)])).encode()))
        for i in range(self.count):
            print((i/(self.count-1))*100)
            if(self.send_dta(i)==1):
                1
            else:
                break
s=server()
s.send_file('d:/kali 2018-4/kali-linux-2018.4-amd64.iso')
s.send_file('d:/kali 2018-4/blackarch-linux-netinst-2019.09.01-x86_64.iso')
s.send_file('d:/kali 2018-4/Qubes-R4.0.1-x86_64/Qubes-R4.0.1-x86_64.iso')
