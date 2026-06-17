def decimalToBinary(n) :
    res = ''
    while n > 0 :
        if n % 2 == 1 :
            res += '1'
        else : 
            res += '0'
        n = n // 2
    
    return res[::-1]

decmtobinary = decimalToBinary(7)
print('decimal to binary' , decmtobinary)
# Time compleixty O(Log2n)
# Space  compleixty O(Log2n)

