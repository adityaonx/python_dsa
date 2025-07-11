def two_sum(nums,target):
    d1={}
    #{value:index}
    #{5:0,1:1,7:2,2:3}
    for i,v in enumerate(nums):
        complement=target-v
        if complement in d1:
            return [d1[complement],i]
        d1[v]=i
    
num_list = [5, 1, 7, 2, 3]
n = 10
print(two_sum(num_list,n))


