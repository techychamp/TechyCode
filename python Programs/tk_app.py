import tkinter as tk
#app
class border(tk.Frame):
    def __init__(self,master,arg={"elem":tk.Button,"prop":{"relief":"flat"},"pk_prop":{}},args={"highlightbackground":"black","highlightcolor":"black","highlightthickness":2}):
        super().__init__(master,args)
        arg["elem"](self,arg["prop"]).pack(arg["pk_prop"])
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        #attributes
        self.attributes("-transparentcolor","grey")
        #childrens
        self.frame=tk.Frame(bg="white")
        self.frame.pack(anchor=tk.NE)
        self.btn1=border(self.frame,{"elem":tk.Button,"prop":{"text":"Search","relief":"flat","bg":"#0080c0","fg":"white"},"pk_prop":{"anchor":tk.NW}})
        self.inpt=tk.Entry(self.frame,bd=2)
        self.inpt.pack(fill="y",side="left")
        self.btn1.pack(side="right")
        #evevnt-binder
        self.evt()
        #menu
        self.menu=tk.Menu()
        self.filemenu=tk.Menu(self.menu,tearoff=0)
        self.filemenu.add_command(label="Reload")
        self.filemenu.add_command(label="Login")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit")
        self.menu.add_cascade(label="File",menu=self.filemenu)
        self.config(menu=self.menu)
    def evt(self):
        self.btn1.bind("<Enter>",lambda x:self.call(self.btn1,x))
        self.btn1.bind("<Leave>",lambda x:self.call(self.btn1,x))
    #event
    def call(self,elem,eve):
        if(eve.type==tk.EventType.Enter):
            prop={"highlightbackground":"#ddd","highlightcolor":"#ddd"}
            prop2={"bg":"#648080","fg":"black"}
        elif(eve.type==tk.EventType.Leave):
            prop={"highlightbackground":"black","highlightcolor":"black"}
            prop2={"bg":"#0080c0","fg":"white"}
        elem.config(prop)
        elem.children.get("!button").config(prop2)
s=app()



