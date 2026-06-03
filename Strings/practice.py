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