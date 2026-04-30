# lists it is mutable
student = ["yest", 'the', 12, 76]
student[0]  = 'nany'
print(student[0:3])
print(student[ :3])
print(student[1:])
print(student[-3:-2])

nums = [10, 9, 8, 7, 26]
# print(list(nums))
print(nums.append(90))
print(nums.sort())
print(nums.sort(reverse=True))
print(nums.reverse())
print(nums.remove(9)) #remove first occurane
print(nums.remove(10))
print(nums.insert(1, 19))
print(nums)

# TUPLES it is mutable
tuple = (8, 5, 2,6,9,2) 
# or tuple = (8, 9, 0, 2,)
print(type(tuple))
print(tuple[0])
# tuple with sinle value
tup = (2, )
print(type(tup))
print(tuple[1:2])
print(tuple.index(2))
print(tuple.count(2))

# Practice questions
# Write a 
# fav1 = input("write your three fav movie movie 1 :")
# fav2 = input(" movie 2 :")
# fav3 = input("movie 3 :")

# movies = [ fav1, fav2, fav3]
# print(movies)

# Pallindrome number
listD = [1,"abc", "abc", 1]
copy = listD.copy()
listD.reverse()
if (listD == copy) :
    print('pallindrome')
else : 
    print("not pallindrome")


# count num ber or students grade
student_grade = ("C", "D", "A", "A", "B", "B", "A")
print(student_grade.count("A"))
stud = list(student_grade)
print(stud.sort())
print(stud)
