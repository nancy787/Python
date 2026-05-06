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