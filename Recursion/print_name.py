def print_name(n) :
    if (n == 0) :
        return 
    
    print('nancy')
    return print_name( n - 1 )

print(print_name(3))

# print 1 to n
def print_n_to_1(num) :
    if num == 0 :
        return 
    print(num)
    return print_n_to_1(num - 1)

print(print_n_to_1(4))

def printnum(curr, num) :
    if curr > num :
        return
    
    print(curr)
    printnum(curr + 1, num)
    return 

printnum(1, 4)

# Sum of n natural number
def sumofNum(n) :
    if n == 1 : 
        return 1
    
    return n + sumofNum(n - 1)
    
print(sumofNum(5))

# Factorial of a number
def factorial(n) : 
    if n == 0 :
        return 1
    
    return n * factorial( n - 1)

print(factorial(5))

def reverse_array(arr) : 
    p1 = 0
    p2 = len(arr) - 1
    while p1 < p2 :
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1

    return arr

num = [5,4,3,2,1]
print(reverse_array(num))

# Fibbonacci 
def fibbo(n) :
    if n <= 1 :
        return n
    
    last = fibbo(n - 1)
    slast = fibbo(n - 2)

    return last + slast

fibbo(5)

# Pallindrome
def pallindrome(start, end) :

    if start >= end :
        return True
    if(num[start] != num[end]) : 
        return False
    
    return pallindrome(start + 1, end - 1)

num = 'nans'
start  = 0
end = len(num) - 1
print(pallindrome(start, end))
    