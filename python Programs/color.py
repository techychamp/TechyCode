def hexify(self,n):
                return "0%s"%(hex(n)[2:]) if(n<16) else hex(n)[2:]