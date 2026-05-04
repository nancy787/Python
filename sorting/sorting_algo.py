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