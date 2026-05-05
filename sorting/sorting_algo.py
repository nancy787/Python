#bubble sort
def bubblesort(nums) :
    n = len(nums)
    for i in range(n - 1) :
        for j in range(n -1 - i) :
            if nums[j] > nums[j+1] :
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


print(bubblesort([13,46,24,52,20,9]))


# selection sort
def selectionSort(nums) :
    n = len(nums)
    for i in range(n) :
        minindex = i
    for j in range(i +1, n) :
        if(nums[j] < nums[minindex]) :
            minindex = j
    nums[i], nums[minindex] = nums[minindex], nums[i]
    return nums

# print(selectionSort([13,46,24,52,20,9]))
# time complexity o(n2)



# insertion sort

def insertionSort(nums) :
    n = len(nums)
    for i in range(1, n) :
        curr = nums[i]
        prev = i - 1

        while prev >= 0 and nums[prev] > curr:
            nums[prev + 1] = nums[prev]
            prev -= 1

        nums[prev + 1] = curr
    return nums
    

print(insertionSort([5, 2, 4, 6, 1, 3]))

# MERGE SORT
def merge(arr, mid, start, end) :
    temp = []
    i = start
    j = mid + 1

    while i <= mid and j <= end :
        if arr[i] <= arr[j] :
            temp.append(arr[i])
            i += 1
        else :
            temp.append(arr[j])
            j += 1

    while i <= mid :
            temp.append(arr[i])
            i +=1
    while j <= end :
            temp.append(arr[j])
            j += 1

    for i in range(len(temp)) :
        arr[start + i] = temp[i]


def mergeSort(arr, start, end) :
    if start < end :
        mid = (start + end) // 2
        mergeSort(arr, start, mid) #left
        mergeSort(arr, mid + 1, end)   #right

        merge(arr, mid, start, end)

mylist = [4,3,2,1]
start = 0
end = len(mylist) - 1
mergeSort(mylist, start, end)
print(mylist)