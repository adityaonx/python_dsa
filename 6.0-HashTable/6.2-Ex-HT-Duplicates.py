def find_dup(ls):
    d1={}
    for item in ls:
        d1[item]=d1.get(item,0)+1
    ls1=[]
    for i,k in d1.items():
        if d1[i]>1:
            ls1.append(i)
    return ls1
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_dup(nums))



