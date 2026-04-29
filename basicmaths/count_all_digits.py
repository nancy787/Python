# count all digits
def countAllDigits(num) :
    counter = 0
    while num > 0 :
        rem = num % 10
        counter = counter + 1
        num = num // 10 

    return counter

result = countAllDigits(1)
print(result)

# Reverse a number

def ReverseNumber(num) : 
    reverse = 0 
    while num > 0 :
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num // 10
    return reverse

print(ReverseNumber(7789))


def Pallindrome(num):
    reverse = 0

    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num // 10

    return reverse


checkNum = 4554

pallindome = Pallindrome(checkNum)

print("pallindrome:", pallindome)

if checkNum == pallindome:
    print('Palindrome Number')
else:
    print('Not Palindrome')

def find_gcd(n1, n2):

    while n1 > 0 and n2 > 0:

        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1

    if n1 == 0:
        return n2

    return n1


gcd = find_gcd(10, 5)
print(gcd)

# Armstrong Number

def armstrong(num) :
    anum = num
    sum = 0
    while num > 0 :
        rem = num % 10
        sum += rem * rem * rem
        num = num // 10
    
    if sum == anum :
        return True
    else : 
        return False

arm = armstrong(152)
print(arm)

# Print all the divisionr
def print_all_divisior(num) :
    divisiors = []
    for i in range(1, num+1) :
        if (num % i) == 0 :
            divisiors.append(i)
    return divisiors

print(print_all_divisior(36))