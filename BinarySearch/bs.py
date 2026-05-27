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


