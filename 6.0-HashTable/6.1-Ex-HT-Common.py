
def is_common(ls1,ls2):
    dc1={}
    for i in ls1:
        dc1[i]=True
    for j in ls2:
        if dc1.get(j):
            return True
    return False
####O(n)
ls2=[2,4,5]
ls1=[1,3,4]
print(is_common(ls1,ls2))