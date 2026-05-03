# While 
# print numbers
# i = 1
# while(i <= 100) :
#     print(i)
#     i += 1

# i = 100
# while(i >= 1) :
#     print(i)
#     i -= 1

# num = int(input('enter numver yo get multiplication'))
# i = 1
# while(i <= 10) :
#     print(num * i)
#     i += 1

# mylist = [1, 4, 9, 16, 26, 36, 49, 64, 81, 100]
# i = 0   

# while(i < len(mylist)) :
#     print(mylist[i])
#     i += 1

# key = (1, 4, 9, 16, 25, 37, 49, 64, 81, 100)
# n = int(input('Enter numer you want to search'))
# i = 0
# while i < len(key) :
#     if( key[i] == n) :
#         print('found')
#         break
#     else :
#         print("not found..")
#     i+= 1

# FOR

# numlist = [1, 2, 3, 4]
# for val in numlist :
#     print(val)
# else : #optionsl
#     print('loop end')

listData = [1, 4, 9, 16, 29, 14, 49, 64, 81, 100]
for val in listData :

    print(val)

for i in range(10) : #ramge stoping condtion
    print(i)

for i in range(2, 10) : #ramge start and stoping condtion
    print(i)

for i in range(2, 100, 2) : #starge start and stiro and step size
    print(i)

for i in range(1, 101) :
    print(i)

for i in range(100, 0, -1) :
    print(i)

num  = int(input('enter nymber'))
for i in range(1, 11) :
    print(num * i)

#pass

sum = 0
n = 10
for i in range(n) :
    sum += n