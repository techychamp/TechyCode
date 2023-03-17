import file_handle,time
class log():
    def __init__(self,file_name):
        self.file=file_handle.file(file_name,"author")
    def encoder(self,text):
        text.append(str(time.time()))
        var=self.merge(text,"-")+"\n"
        return var
    def decoder(self,text):
        text=text.split("-\n")[0:-1]
        return [i.split("-")[0:-1]+[time.ctime(float(i.split("-")[-1]))] for i in text]
    def log_write(self,ltext,clear=False):
        self.file.write(self.__encoder__(ltext),clear)
    def log_read(self,line_no=0,flg=0):
        if(flg==0):
            return self.decoder(str(bytes(self.file.read()).decode()))
        else:
            return self.decoder(str(bytes(self.file.read(line_no,1)).decode()))
    def merge(self,text,sep=" "):
        string=''
        for i in text:
            string+=i+sep
        return string
        
fil=log("d:/projects/text.txt")


        
        
