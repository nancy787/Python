# Finding Sqrt of a number using Binary Search

def sqrt(n) : 
    for i in range(n) :
        if i * i == n :
            return i 
    return -1

findSqrt = sqrt(36) 
print('find_sqrt', findSqrt)

# Optimal methood

def SquareRoot(n) :
    low = 1 
    high = n
    ans = 1
    while(low <= high) : 
        mid = (low + high )// 2
        if mid * mid <= n :
            ans = mid 
            low = mid + 1
        else :
            high = mid - 1
    
    return ans
        

square_root = SquareRoot(36) 
print('square_root', square_root)

# Nth Root of a Number using Binary Search
def nthRoot(n, m) :
    low = 1
    high = m

    while low <= high :
        mid = (low + high) //2
        value = mid ** n
        if value == m :
            return mid
        elif value < m :
            low = mid + 1

        else :
            high = mid - 1

    return -1

nth_rooot = nthRoot(3, 27) 
print('nth_rooot', nth_rooot)
# Time Complexity: O(log m)
# Space Complexity: O(1)