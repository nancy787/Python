


# Binary Search

def BinarySearch(nums, target) :
    low = 0
    high = len(nums) - 1

    while low <= high :
        mid = (low + high)// 2
        if nums[mid] == target :
                return mid
        elif target > nums[mid] :
                low = mid + 1
        else :
                high = mid - 1

    return -1

nums = [2,4,6,7,9,12,16,17]
binary_search = BinarySearch(nums, 9)
print(binary_search)


def RecursiveBinarySearch(nums, low, high, target) :
    if low > high :
        return - 1
    mid = (low + high )//2

    if nums[mid] == target :
        return mid
    elif target > nums[mid] :
         return RecursiveBinarySearch(nums, mid + 1, high, target)
    else :
       return RecursiveBinarySearch(nums, low, mid - 1, target)


nums = [2,4,6,7,9,12,16,17]
low = 0
high = len(nums) - 1
search = RecursiveBinarySearch(nums, low, high, 9)
print(search)

# Time complexity 
# O(log2n)

def lowerBoundBruteForce(arr, x) :
    arr.sort()
    n = len(arr) - 1
    for i in range(n) :
        if arr[i] >= x :
            return i
    return n
arr = [3,5,8,15,19]
lower_bound = lowerBoundBruteForce(arr, 9)
print(lower_bound)

# Timecomplity 0(N)


def lowerBound(arr, x) :
    low = 0
    high = len(arr) - 1
    ans = x
    while (low <= high) :
        mid = (low + high)//2
        if(arr[mid] >= x) : #lower bound
            ans = mid
            high = mid - 1
        else : 
            low = mid + 1
    
    return ans


arr = [3,5,8,15,19]
lower_bound = lowerBound(arr, 9)
print('lower_bound', lower_bound)


def upperBound(arr, x) :
    low = 0
    high = len(arr) - 1
    ans = x
    while (low <= high) :
        mid = (low + high)//2
        if(arr[mid] > x) :  #Upper bound 
            ans = mid
            high = mid - 1
        else : 
            low = mid + 1
    
    return ans

arr = [3,5,8,15,19]
upper_bound = upperBound(arr, 9)
print('upper_bound', upper_bound)


def BinarySearchInsert(arr, x) :
    n = len(arr)
    low , high = 0, n - 1
    ans = n
    while(low <= high) : 
        mid = (low + high) // 2

        if(arr[mid] >= x) :
            ans = mid
            high  = mid - 1
        else :
            low = mid + 1

    return ans

arr = [1,2,4,7]
insert_elem = upperBound(arr, 2)
print('insert_elem', insert_elem)

def firstAndLastoccurance(nums, target) :
    low = 0
    high = len(nums) - 1
    first  = -1
    while low <= high :
        mid = (low + high) //2
        if nums[mid] == target :
            first = mid
            high = mid - 1
        elif target > nums[mid]: 
                low = mid + 1
        else :
            high = mid - 1
        
    if first != -1 and first + 1 < len(nums) and nums[first + 1] == target:
        return first + 1

    return - 1
nums = [3, 4, 13, 13, 13, 20, 40]
occurance = firstAndLastoccurance(nums, 13)
print('occurance', occurance)



def countOccurance(nums, elem) : 
    count = 0
    for i in range(len(nums) - 1) :
        if nums[i] == elem : 
                count += 1
    return count

nums = [2, 2 , 3 , 3 , 3 , 3 , 4]
count_occurance = countOccurance(nums, 3)
print('count_occurance', count_occurance)
# Timecomoelxity O(n)
# Space o(1)


# Search Element in a Rotated Sorted Array

def Searchelement(nums, k) :
    for i in range(len(nums)) :
        if nums[i] == k :
            return i
    return -1

elem = [1,3]
search_emel = Searchelement(elem, 3)
print('elem_position', search_emel)

# Timecompleity 0(N)
def searchElementOptimal(nums, k):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == k:
            return mid 
        if nums[low] <= nums[mid]:
            if nums[low] <= k < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < k <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1



nums = [4,5,6,7,0,1,2]
search_elem = searchElementOptimal(nums, 0)
print(search_elem)
# Timecomplexity O(logn)

def elementSearch(nums, k) :
    for i in range(len(nums)) :
        if nums[i] == k :
            return True
    return False

elem = [1,3]
search_emel = elementSearch(elem, 3)
print('elem_position', search_emel)



def minimumSortedElem(nums) :
    minElem = nums[0] 
    for i in range(len(nums) - 1) :
        if nums[i] < minElem : 
            minElem = min(minElem, nums[i])

    return minElem

elem = [4,5,6,7,0,1,2,3]
min_sorted = minimumSortedElem(elem)
print('minimim_sorted', min_sorted)
# O(n)
# O(1)

def singleSearch(nums) :
    setElem = {} 
    for num in nums :
        if num in setElem :
            setElem[num] += 1
        else :
            setElem[num] = 1

    for key, value in setElem.items() :
        if value == 1 :
            return key
    return -1
elem = [1,1,3,2,5,5]
single_search = singleSearch(elem)
print('single_search', single_search)

# time O(n)
# Space O(n)

def PeakElement(nums) :
    for i in range(1, len(nums) - 1) :
        if nums[i] >  nums[i - 1] and nums[i] > nums[i+1] :
                return i
    return -1 

elem = [1,2,3,4,5,6,7,8,5,1]
peak_element = PeakElement(elem) 
print('peak_element', peak_element)