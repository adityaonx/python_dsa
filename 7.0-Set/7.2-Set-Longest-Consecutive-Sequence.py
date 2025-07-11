def long_cons_seq(nums):
    nums.sort()
    #[1,2,4,5,6,7,8,100,200]
    start=None
    for i in range(len(nums)-1):
            if start is None and nums[i]+1==nums[i+1]:
                  start=nums
            
            
        
        


nums = [100, 5, 6, 7, 8, 200, 1, 2, 4]
long_cons_seq(nums)
