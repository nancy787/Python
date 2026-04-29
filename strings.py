str1 = 'nancy',
str2 = "nancy2",
str2 = """nancy"""
print(len(str2))
print(str2[0:3]) #slicing
print(str2[0 :]) #slicing
print(str2[-3 : -1]) #slicing nancy

# String methods
str = "python i am studying python"
print(str.endswith('on')) #it return true or false if string is eids with
print(str.capitalize())  #it captalise firs string
print(str.replace('a', 'n')) #replace with old to new
print(str.find('python')) #check if exits in the the string if yes then it gave starting index of that finded char
print(len(str))
print(str.count("python")) #count how many times charcter exitss


name = input('Enter your first name :')
print('your name has :', len(name), 'charachers')

ocur = 'this is my $ $ $string $ $'
print(ocur.count('$'))