def find_pairs(ar1,ar2,tgt):
    set1=set(ar1)
    pairs=[]
    for i in ar2:
        compliment=tgt-i
        if compliment in set1:
            pairs.append((compliment,i))
    print(pairs)
arr1 = [0,1,2]
arr2 = [7,8,9]
target = 10
find_pairs(arr1,arr2,target)
