def cgpa(mark:list,credit:list)->int:
    if(len(mark)==len(credit)):
        return sum([x*y for x,y in zip(mark,credit)])/sum(credit)
    else:
        raise Exception("length mismatch error")
crdt,mrk=[],[]
credit,mark=[],[]
credit=[]
mark=[]
mrk,crdt=mrk+mark,crdt+credit
print("Ttl",cgpa(mrk,crdt))
