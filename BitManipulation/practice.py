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

def BinaryToDecimal(str) :
    p2 = 1
    num = 0

    for i in range(len(str) - 1, -1, -1) :
        if str[i] == '1' :
            num = num + p2
        p2 = p2 * 2
    
    return num

str = '1101'
decimal_to_binary = BinaryToDecimal(str)
print('decimal to binary' , decimal_to_binary)
# Time complxity O(len)
# Time complxity O(1)
