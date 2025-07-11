def first_non_rep(s1):
    d1={}
    for i in s1:
        d1[i]=d1.get(i,0)+1
    for i,k in d1.items():
        if k<2:
            return i
string1 = 'hhello'
print(first_non_rep(string1))



