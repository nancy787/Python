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

# Isomorphic String
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}
    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]

        if c1 in s_to_t and s_to_t[c1] != c2:
            return False

        if c2 in t_to_s and t_to_s[c2] != c1:
            return False

        s_to_t[c1] = c2
        t_to_s[c2] = c1

    return True

print('Isomorphic')
print(is_isomorphic("egg", "add"))     # True
# print(is_isomorphic("foo", "bar"))     # False
# print(is_isomorphic("paper", "title")) # True
# print(is_isomorphic("badc", "baba"))   # False
# Timecomplexit O(nlign)
# Space o(1)

# Longest Common Prefix
def longest_common(words) :
    words.sort()
    n = len(words) - 1
    ans = ""
    first_str = words[0]
    last_str = words[n]

    for i in range(0, n) :
        if first_str[i] == last_str[i]  :
            ans += first_str[i]

    return ans  

print('longest_common')
str = ["apple", "banana", "grape", "mango"]
print(longest_common(str))  



# Largest odd number
def largestOddNum(str) :
    str = int(str)
    
    maxstr = 0
    while str > 0 :
        rem = str % 10
        if str % 2 != 0 :
            maxstr = max(maxstr, str)
        str = str // 10

    return maxstr

print('larger_odd')
print(largestOddNum("0214638"))  
# timecompelity 0(nlogn )


def valid_paranthesis(str) :
    count = 0
    result = ''
    for s in str :
        if s == '(' :
            if count > 0 :
                result += s
                count+= 1
            elif s == ')' :
                count -= 1
                if count > 0 :
                    result += s
            if count < 0 :
                return False

    return result

print('valid_paranthesis')
s = "((()))" 
print(valid_paranthesis(s))  

def sortCharByFreq(str) :
    result = {} 
    for s in str :
        if s in result :
            result[s] += 1
        else : 
            result[s] = 1
    

        sorted_data_desc = dict(
            sorted(
                result.items(),
                key=lambda item: (-item[1], item[0])
            )
        )


    return list(sorted_data_desc.keys())

print('sort_char')
print(sortCharByFreq("tree"))  
# timecompelity 0(nlogn )

def reverseWords(str) :
    str = str.split()
    result = []
    for i in range(len(str) - 1, -1, -1) :
        result.append(str[i])

    return " ".join(result)
print('reverse_words')
word = "welcome to the jungle"
print(reverseWords(word))  
# Time complexoyy 0(n)
# Space Complexut 0(n) //result list

def reverseString(str) :
    str = str.split()
    low = 0
    high = len(str) - 1
    
    while low < high :
        [str[low], str[high]] = [str[high], str[low]]
        low+= 1
        high -= 1

    return str

print('reverse_string_optimal')
word = "welcome to the jungle"
print(reverseWords(word)) 
# Timecompledxty o(nLogn)

# Maximum Nesting Depth of Parenthesis
def maximumDepth(str) :
    count = 0
    result = 0

    for s in str :
        if s == '(' :
            count+= 1
        elif s == ')' :
            count -= 1
        if count > result :
            result = count

    return result

print('maximum_depth')
s = "(1)+((2))+(((3)))"
print(maximumDepth(s)) 


# Convert roman to integer
def RomantoInt(roman) :
    val = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50, 
        'C' : 100,
        'D' : 500, 
        'M' : 1000
    }

    result = 0

    for i in range(0, len(roman) - 1) :
        if roman[i] not in val :
            return 'Invalid roman'

        if  val[roman[i+1]] > val[roman[i]]:
                result -=  val[roman[i]]
        else : 
            result += val[roman[i]]

    return result + val[roman[-1]]

print('roman_to_int')
s = "LVIII"
print(RomantoInt(s)) 

# timecomplexty = O(n)
# space compelxty O(n)

def atoi(str) :
    result = 0
    str = str.strip()
    sign = 1
    if str[0] == '-' :
        sign = -1

    for i in range(0, len(str)) :
        if str[i].isdigit() :
            result =  result * 10 + int(str[i])
        else :
            break

    return result * sign

print('atoi')
s = "words and 987" 
print(atoi(s)) 

# Longest Subsctring

def atMostKDistinct(s, k) :
    freq = {}
    l, r = 0, 0
    maxlength = 0
    while r < len(s)     :
        freq[s[r]] = freq.get(s[r], 0) + 1

        while(len(freq) > k) :
            freq[s[l]] -= 1
            if freq[s[l]] == 0 : 
                del freq[s[l]]
            l+= 1

        if(len(freq) <= k) :
            maxlength = max(maxlength, r - l + 1)

        r = r+1

    return maxlength

print('dist substring count')
s = "pqpqs" 
print(atMostKDistinct(s, 2)) 
# Time complexity O(n)
# Space compelcity O(n)