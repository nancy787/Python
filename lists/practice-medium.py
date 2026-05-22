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

# Dutch National Algorithm

def DutchNationalFlag(nums) :
    low = 0
    high = len(nums) - 1
    mid = 0

    while mid <= high :
        if nums[mid] == 0 :
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1 :
            mid += 1
        else :
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

print(DutchNationalFlag([1, 0, 2, 1, 0]))
# Timecolexity O(1)
# Spaceconoeksty O(1)

# Find the Majority Element that occurs more than N/2 times
def majorityElement(nums) :
    myset = {}
    for num in nums :
        if num in myset :
            myset[num] += 1
        else :
            myset[num] = 1


    for key,count in myset.items() :
        if count > 2 :
            return key

    return -1

print(majorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7]))
# Timecomplexity O(n2)
# Space Complexity O(1)

def majorityElementOptimal(nums) :
    count = 0
    element = 0

    for num in nums :
        if count == 0 :
            element = num
            count += 1
        elif  element == num :
                count += 1
        else : 
            count -= 1

    cnt1 = nums.count(element)
    
    if cnt1 > (len(nums) // 2):
        return element
    
    return -1
print(majorityElementOptimal([7, 0, 0, 1, 7, 7, 2, 7, 7]))
# Timecompelixty O(n)

# Kadans Algorithm maxmimum sum subarray

def MaxSubarraySum(nums) :
    sum = 0
    maxi = float('-inf')
    for i in range (0, len(nums)) :
        if sum == 0 :
            start = i
        sum += nums[i]
        if sum > maxi :
            maxi = sum

        if sum < 0 :
            sum = 0
    return maxi

print(MaxSubarraySum([2, 3, 5, -2, 7, -4]))
# Timecomplexity O(n) Space O(1)

# STock buy and sell
def buyandSell(num):
    maxprofit = 0
    n = len(num)

    for i in range(n):
        for j in range(i + 1, n):
            profit = num[j] - num[i]
            maxprofit = max(maxprofit, profit)

    return maxprofit

buynsell = buyandSell([7,6,4,3,1])
print(buynsell)

# Timecomplexity = O(n2)
# Space complirxy O(1)

# Buy and sell optimals
def buysellopt(num) :
    minsofar = num[0]
    maxprofit  = 0
    profit = 0
    for i in range (1, len(num) - 1)  :
        minsofar = min(minsofar, num[i])
        profit = num[i] - minsofar 
        maxprofit =  max(maxprofit, profit)
    return maxprofit

maxprofit = buysellopt([7,1,5,3,6,4])
print(maxprofit)
# timecompexity 0(n)
# space compleicty O(1)

# Rearrange array
def rearrangeElement(nums):
    n = len(nums) - 1
    positiveArray = []
    negativeArray = []

    for num in nums:
        if num > 0:
            positiveArray.append(num)
        else:
            negativeArray.append(num)

    for i in range(n//2):
         nums[2 * i] = positiveArray[i] 
         nums[2 * i + 1] = negativeArray[i] 

    return nums


rearrange = rearrangeElement([1,2,-3,-1,-2,-3])
print(rearrange)
# Timecompexity is O(n2)
# space compelity O(n)

#Op