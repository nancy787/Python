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