import tkinter as tk
class App():
    def __init__(self):
        self.__prev__='c'
        i=5
        self.__root__=tk.Tk()
        self.__root__.geometry("180x145")
        self.__root__.resizable(0,0)
        self.__disp__=self.__element__(tk.Label,self.__root__,text="0")
        self.__disp__.grid(column=0,rowspan=2)
        self.__disp1__=self.__element__(tk.Label,self.__root__,text="")
        self.__disp1__.grid(column=0,rowspan=1)
        frame=self.__element__(tk.Frame,self.__root__,relief="ridge")
        frame.grid()
        frame.grid_columnconfigure((0,1,2,3),minsize='16px')
        self.__element__(tk.Button,frame,text="1",width=i,command=self.__click__("1")).grid(column=0,row=0)
        self.__element__(tk.Button,frame,text="2",width=i,command=self.__click__("2")).grid(column=1,row=0)
        self.__element__(tk.Button,frame,text="3",width=i,command=self.__click__("3")).grid(column=2,row=0)
        self.__element__(tk.Button,frame,text="+",width=i,command=self.__click__("+")).grid(column=3,row=0)
        self.__element__(tk.Button,frame,text="4",width=i,command=self.__click__("4")).grid(column=0,row=1)
        self.__element__(tk.Button,frame,text="5",width=i,command=self.__click__("5")).grid(column=1,row=1)
        self.__element__(tk.Button,frame,text="6",width=i,command=self.__click__("6")).grid(column=2,row=1)
        self.__element__(tk.Button,frame,text="-",width=i,command=self.__click__("-")).grid(column=3,row=1)
        self.__element__(tk.Button,frame,text="7",width=i,command=self.__click__("7")).grid(column=0,row=2)
        self.__element__(tk.Button,frame,text="8",width=i,command=self.__click__("8")).grid(column=1,row=2)
        self.__element__(tk.Button,frame,text="9",width=i,command=self.__click__("9")).grid(column=2,row=2)
        self.__element__(tk.Button,frame,text="*",width=i,command=self.__click__("*")).grid(column=3,row=2)
        self.__element__(tk.Button,frame,text="0",width=i,command=self.__click__("0")).grid(column=0,row=3)
        self.__element__(tk.Button,frame,text="c",width=i,command=self.__click__("c")).grid(column=1,row=3)
        self.__element__(tk.Button,frame,text="=",width=i,command=self.__click__("=")).grid(column=2,row=3)
        self.__element__(tk.Button,frame,text="/",width=i,command=self.__click__("/")).grid(column=3,row=3)
        self.__root__.mainloop()
    def __element__(self,elem,parent,**arg):
        return elem(parent)if(arg==0)else elem(parent,arg)
    def __click__(self,val):
        if(val!="c"):
            if(val not in ['+','-',"*","/","="]):
                return lambda :self.__add__(val)
            else:
                return lambda :self.__add__(val)if((self.__calc__())&(val!='='))else self.__calc__()
        else:
            return lambda :1 if((self.__disp1__.config(text="")==None)&(self.__disp__.config(text="0")==None))else 0
    def __calc__(self):
        if(len(self.__disp1__.cget("text"))!=0):
            self.__disp__.config(text="")
            self.__disp__.config(text=str(eval(self.__disp1__.cget("text"))))
        return 1
    def __add__(self,val):
        if((((self.__prev__).isnumeric()!=True)|(self.__disp1__.cget("text")==""))&(val=='0')):
            return
        self.__disp1__.config(text=self.__disp1__.cget("text")+val)
        self.__prev__=val
s=App()
