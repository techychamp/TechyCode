class water_management:
    def __init__(self):
        self.days=int(input("Enter number of days :"))
        self.clust_count=int(input("Enter number of clusters :"))
        self.clust=[input("").split(" ") for i in range(self.clust_count)]
        self.clust={i[0]:{"object":cluster((int(i[1]),int(i[2]),0)),"childrens":dict()} for i in self.clust}
        self.pipe_cnt=int(input("pipeline count :"))
        self.pipe=dict()
        for i in range(self.pipe_cnt):
            self.piper()
        self.needed=0
        self.trigger()
        print(self.needed)
    def trigger(self):
        for day in range(self.days):
            self.needed+=self.filler(self.pipe)
            self.use_water(self.pipe)
    def filler(self,obj):
        if(obj=={}):
            return 0
        else:
            temp=0
            for i in obj:
                val=self.filler(obj[i]["childrens"])
                if(val==0):
                    temp+=obj[i]["object"].fill()
                else:
                    temp+=val
                    temp+=obj[i]["object"].fill(1)
            return temp
    def use_water(self,obj):
        if(obj=={}):
            return 0
        else:
            for i in obj:
                val=self.use_water(obj[i]["childrens"])
                if(val==0):
                    obj[i]["object"].use()
                else:
                    obj[i]["object"].use()
        return 1
    def piper(self):
        value=input("").split("_")
        if(value[0].upper()=="F"):
            self.pipe.update({value[1]:self.clust[value[1]]})
        else:
            self.child_update(value[0],self.pipe)[value[0]]["childrens"].update({value[1]:self.clust[value[1]]})
    def child_update(self,name,obj):
        if(name in obj):
            return obj
        else:
            temp=dict()
            for i in obj:
                val=self.child_update(name,obj[i]["childrens"])
                if(val!={}):
                    temp=val
                    break
            return temp  
            
class cluster:
    def __init__(self,val):
        self.need,self.capacity,self.have=val
    def fill(self,do=0):
        if(self.have>=self.need)and(not(do)):
            return 0
        else:
            self.have=self.capacity
            return self.capacity
    def use(self):
        self.have-=self.need
        return 1
w=water_management()
                
        
