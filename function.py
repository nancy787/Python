def printlistlen(list) :
    return len(list)

print(printlistlen([2,3,4,2]))

def printelemn(list) :
    n = len(list)
    for i in range(n) :
        print(list[i], end=" ")

print(printelemn([2,3,4,2]))


def factorial(n) :
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i 
    return fact

print(factorial(5))

def factorial1(n) :
    fact = 1
    if n < 0 :
        return 1
    fact = n * factorial(n - 1)
    return fact

print(factorial1(5))


def usdToInr(usd) :
    exchange_rate = 95.13
    inr = usd * exchange_rate 
    return inr

print(usdToInr(5))

def sum1(num) : 
    sum = 0
    if num < 0 :
        return 1
    sum = num + sum1(num - 1)
    return sum

print(sum1(5))

def printlist(nums, idx) :
    if(idx == len(nums)) :
        return
    print(nums[idx])
    printlist(nums, idx + 1)

    return 

print(printlist([1,2,3,4,8], 4))