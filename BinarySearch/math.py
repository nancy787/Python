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

