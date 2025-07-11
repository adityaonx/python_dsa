def ana(ls):
    d1={}
    for string1 in ls:
        count=[0]*26
        for letter in string1:
            count[ord(letter)-97]=1
        if not d1.get(tuple(count)):
            d1[tuple(count)]=[]
        d1[tuple(count)].append(string1)
    
    new_ls=[]
    for i,k in d1.items():
        new_ls.append(k)
    return new_ls
list1=["eat", "tea", "tan", "ate", "nat", "bat"]
print(ana(list1))


