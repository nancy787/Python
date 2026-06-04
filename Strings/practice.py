# Reverse Words in a String
def revstring(str) :
    str = str.split()
    result = []

    for i in range(len(str) -1, -1, -1) :
        result.append(str[i])

    return " ".join(result)

str = " the sky is blue " 
reverse_string = revstring(str)
print(reverse_string)
# Time complexity o(n)

# Largest odd numberr in string
def largestOddNumbe(str) :

    ind = -1
    i = 0
    for i in range(len(str) -1, -1, -1) :
        if int(str[i]) % 2 == 1 :
            ind = i
            break
    
    while i <= ind and str[i] == '0' :
            i+= 1

    return str[i:ind + 1]

largest_odd = largestOddNumbe("0214638")
print(largest_odd)
# Time complexity o(n)

def Ananagram(str1, str2) :

    l1 = len(str1)
    l2 = len(str2)

    if l1 != l2 :
        return False

    str1 = "".join(sorted(str1)) #O(n log n)
    str2 = "".join(sorted(str2)) #O(n log n)
    i = 0

    while i < l1 : #O(n)
        if str1[i] != str2[i] : 
            return False
        i += 1

    return True

anagram = Ananagram("RULES", "LESRT" )
print(anagram)

# Time complexity is O(n log(n))
# O(n)

# Check if one string is rotation of another
def checkrotatedString(str, goal) : 
    d = 1
    n = len(str)
    for i in range(0, n - 1) :
        shift = d % n
        left_rotated = str[shift:] + str[:shift]

        if left_rotated == goal : 
            return True
        d += 1
    
    return False

rotated = checkrotatedString("rotation", "tionrota" )
print(rotated)
# Timecopkecyu O(n)
# Space Complity O(n)