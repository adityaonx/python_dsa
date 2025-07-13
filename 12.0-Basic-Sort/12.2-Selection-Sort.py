def sel_sort(ls):
    for i in range(len(ls)-1):
        min_index=i
        for j in range(i+1,len(ls)):
            if ls[j]<ls[min_index]:
                min_index=j
        ls[min_index],ls[i]=ls[i],ls[min_index]
    return ls            
                
            
    
ls=[4,2,6,5,1,3]
print(sel_sort(ls))
