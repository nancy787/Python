# Find the Largest element in an array
def largest(arr) :
    max = arr[0]
    for i in range(0, len(arr)) :
        if arr[i] > max :
            max = arr[i]
    return max

print(largest([8, 10, 5, 7, 9]))
# time complexity  - o(n)
# space complexity = o(n)

#Find Second Smallest and Second Largest Element in an array
def secondLargest(arr) :
    max = arr[0]
    secondLarge = -1
    for i in range(1, len(arr)) :
        if secondLarge > max :
            secondLarge = max
            max = arr[i]
        elif arr[i] > secondLarge and arr[i]!=  max:
            secondLarge = arr[i]

    return secondLarge

print(secondLargest([1, 2, 4, 7, 7, 5]))
# time complesity o(n)
# space complecity o(n)

# Check if an Array is Sorted
def issorted(arr) :
    for i in range(len(arr) - 1) :
        if arr[i] > arr[i + 1] :
            return False

    return True

print(issorted([5,4,6,7,8]))
# time complexity o(n)

# Remove Duplicates in-place from Sorted Array


def removeDuplicates(nums) :
    myset = set()
    i = 0
    for num in nums :
        if num not in myset :
            myset.add(num)
            nums[i] += 1

    return myset

print(removeDuplicates([1,1,2,2,2,3,3]))
# time complexity o(n)
# space complexity o(n)

def removeDuplicatesTwoPointers(nums) :
    if not nums :
        return 0 
    i = 0
    for j in range(1, len(nums)) :
        if nums[j] != nums[i] :
            nums[i] += 1
            nums[i] = nums[j]

    return i + 1


nums = [1,1,2,2,3]
k = removeDuplicatesTwoPointers(nums)

print(k)
print(nums[:k])

# Left Rotate the Array by One

def leftRotate(nums) :
    temp = nums[0]
    for i in range(1, len(nums)) : 
        nums[i - 1] = nums[i]

    nums[len(nums) - 1] = temp

    return nums
rotate = leftRotate([1, 2, 3, 4, 5])
print(rotate)

# Left rootate by k elemnets

def reverseElement(nums, start, end) :
    while start < end :
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def RotateElemments(nums, k, direction) :
    n = len(nums)
    k = k % n

    if direction == 'right':
        reverseElement(nums, 0, n - 1)  
        reverseElement(nums, 0, k - 1)
        reverseElement(nums, k, n- 1)

    if direction == 'left' :
        reverseElement(nums, 0, k - 1)
        reverseElement(nums, k, n - 1)
        reverseElement(nums, 0, n - 1)
    return nums

def main() :
    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    direction = 'left'
    elem =  RotateElemments(nums, k, direction)
    print(elem)

main()



# Move all Zeros to the end of the array

def moveZeroes(nums) :
    temp = []
    ze = nums.count(0)

    n = len(nums)
    for i in range(0, n) :
        if nums[i] > 0 :
            temp.append(nums[i])
    
    for i in range (ze) :
        temp.append(0)

    return temp

zeros = moveZeroes([0, 1, 0, 3, 12])
print(zeros)

#  O(n2)

def moveZeroTwoPointers(nums) :
    j = 0
    for i in range(0, len(nums)) :
        if nums[i] != 0 :
            nums[i], nums[j] = nums[j], nums[i]  
            j+= 1
    return nums 

movezero = moveZeroTwoPointers([0, 1, 0, 3, 12])
print(movezero)

# Linear Search 
def linearSearch(nums, key) :
    for i in range(0, len(nums)) :
        if nums[i] == key :
            print(f"{key} is present at the {0}th index of the array.")
            return
    return "key is not preset in the given list"

search = linearSearch([1, 2, 3, 4, 5], 31)
print(search)

# union of twi shorted array

def unionofTwoSortedArray(arr1, arr2) :
    i = 0
    j = 0
    union = []

    while(i < len(arr1) and j < len(arr2)) :
        if arr1[i] < arr2[j] :
            if len(union) == 0 or union[-1] != arr1[i] :
                union.append(arr1[i])
            i+= 1
        elif arr1[i] > arr2[j] :
            if len(union) == 0 or union[-1] != arr2[j] :
                union.append(arr2[j])
            j+= 1
        else :
                if len(union) == 0 or union[-1] != arr1[i] :
                    union.append(arr1[i])
                i+= 1
                j+= 1
    
    while( i < len(arr1)) :
        if len(union) == 0 or union[-1] != arr1[i] :
            union.append(arr1[i])
        i+=1
    
    while(j < len(arr2)) :
        if len(union) == 0 or union[-1] != arr2[j] :
            union.append(arr2[j])
        j+= 1

    return union

result = unionofTwoSortedArray([1, 2, 2, 3, 4], [2, 3, 5])
print(result)

# Time and space compliexity O(n + m)
def unionset(arr1, arr2) : 
    union = sorted(set( arr1 + arr2))
    return union
result1 = unionset([1, 2, 2, 3, 4], [2, 3, 5])
print(result1)

# O((n + m) log(n + m))

# Find The missing number
def missingNumber(nums) :
    sum = 0
    n = len(nums) + 1
    expected_result = n *  (n + 1) //2
    for val in nums  :
        sum += val

    return expected_result - sum

ans = missingNumber([8, 2, 4, 5, 3, 7, 1])
print(ans)


# Count Maximum Consecutive One's in the array
def maxConsecutiveOne(nums) :
    counter = 0
    max_count = 0
    for i in range(0, len(nums)) :
        if nums[i] != 1 :
            counter = 0
        else :
            counter += 1
            max_count = max(counter, max_count)

    return max_count

res = maxConsecutiveOne([1, 1,1,1, 0, 1, 1, 1])
print("res", res)

# Find the number that appears once, and the other numbers twice
def getSingleElement(nums) :
    cnt = {}
    for val in nums :
        if val in cnt :
            cnt[val] += 1
        else :
            cnt[val] = 1

    for key, val in cnt.items() :
            if val == 1 :
                res = key

    return res
        
op = getSingleElement([9,1,2,1,2])
print("op", op)

# on2
def getSingleElem(nums) :
    res = 0
    for num in nums :
        res ^=num 

    return res

se = getSingleElem([4,1,2,1,2])
print("se", se)

# FIND SUBARRAY

def subarray(arr) :
    n = len(arr)
    for i in range(0, n) :
        for j in range(i, n) :  
            for k in range(i, j + 1) :
                print(arr[k], end=" ")
        print()
subarr = subarray([10,5,2,7,1]) 
print(subarr)
