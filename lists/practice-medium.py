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

# Sort an array of 0s, 1s and 2s


def sort0s(nums) :
    n = len(nums) - 1
    for i in range(0, n) :
        for j in range(0, n) :
            if nums[j] > nums[j + 1] :
                    nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

print(sort0s([1, 0, 2, 1, 0]))
# Time complexity O(n2)
# space compelicty 

def twoColors(nums) :
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0
    for num in nums :
        if num == 0 :
            cnt_0 += 1
        elif num  == 1 :
            cnt_1 += 1
        else :
            cnt_2 += 1
    
    index = 0
    for i in range(cnt_0) :
        nums[index] = 0
        index += 1
    
    for i in range(cnt_1) :
        nums[index] = 1
        index += 1
    
    for i in range(cnt_2) :
        nums[index] = 2
        index += 1
    
    return nums

print(twoColors([1, 0, 2, 1, 0]))
# Time compelic O(2N)

