# Two sum

def twoSum(nums, target) :
    n = len(nums)
    sum = 0
    for i in range(n) :
        for j in range(i + 1, n) :
            sum = nums[i] + nums[j]
            if sum == target :
                print('Yes')
                print(nums[i], nums[j])
            
print(twoSum([2,6,5,8,11], 14))
# Time complexity = O(n2)
# Space comlexity = O(1)

#using greedy approach

def SumTwo(nums, target) :
    left = 0
    n = len(nums)
    right = n - 1
    nums.sort()

    while left < right :
        if nums[left] + nums[right] < target :
            left += 1
        
        elif nums[left] + nums[right] > target :
            right -= 1
        
        else : 
            nums[left] + nums[right] == target 
            print(nums[left], nums[right]) 
            return 'yes'

    return [-1, 1]

print(SumTwo([2,6,5,8,11], 14))

# time complexity O(n log n)
# Space o(1)
