def bubble_sort(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls
ls=[4,2,6,5,1,3]
print(bubble_sort(ls))