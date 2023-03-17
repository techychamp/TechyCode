import os
def file_name_check(name,direc,cu=1,last=1,lister=[]):
        if((name[0]+str(cu)+'.'+name[1]) not in direc):
                lister.append(cu)
        if(cu!=last):
            return file_name_check(name,direc,cu+1,last,lister)
        else:
            return lister