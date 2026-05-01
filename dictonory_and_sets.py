# dictonory useed to store data values in key:value pair
user =  {
    "name" : "nancy",
    "designation" : 'ai developer',
    "age" : 25,
    "isAdlut" : True,
    "salary per month" : "300000",
    "what_else" : [
        'youtube' , 'tecies',
        'office' ,"techies"
    ],  
    "master" : ("Ai", "Codinh")

}

print(type(user))
user["surname"] = "bhagat"
print(user)

#nesting
# DIctornory methods

# print(list(user.keys()))
# print(len(user.keys()))
print(user.values())
print(user.items())
print(user.get("mast2er")) #it will get the user data if not exists it wil return none
# print(user["master2"]) #it will get the user data if not exists it wil return array

newUser = {"name" : "bhagat"}
user.update(newUser) 
print(user)

# SETS
myset = {1, "@" , 2, 4, 2}
print(myset)
print(type(myset))
print(len(myset))
# crwate empty set
collection = set()
print(collection.add(2))
print(collection.add(3))
print(collection.add(4))
print(collection.add(2))
print(collection.add((2,3,3)))
collection.pop()
print(collection)


set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))


# store word
mydict = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(mydict)

subjects = { "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c "}
print(len(subjects))

marks = {}
# marks1 = input("enter your marks1")
# marks2 = input("enter your marks2")
# marks3 = input("enter your marks3")
# marks.update({ "mark1" : marks1,  "mark2" : marks2,  "mark3" : marks3 })
# print(marks)

myset1 = {9, "9.0"}
myset2 = {
     ("int", 9),
     ("float", 9.0)

    }

print(myset2)