def minimizeArrayValue(nums):
    idx = nums.index(max(nums))
    if idx == 0:
        return nums[idx]
    def check(idx):
        for i in range(idx,0,-1):
            if nums[idx-1] < nums[idx]:
                pass
            else:
                return False
        return True
    while check(idx):        
        temp = idx
        nums[temp] -=1
        nums[temp-1] +=1
        while temp < len(nums)-1:
            if nums[idx] == nums[temp+1]:
                nums[temp+1] -=1
                nums[temp]  +=1
                temp +=1
            else:
                temp +=1
    return nums[idx]
nums = [3,7,1,6]
print(minimizeArrayValue(nums))
