# r - reading
# w - open fro writing, truncate file firs
# x - create a new file and open it for writing
# a - open for writing, appending to the end of the file if it exists
# b - binary mode
# t - text mode
# + - open dusk file for updating


# file = open('demo.txt' , 'r')
# data = file.read() 
# line1 = file.readline()
# print(line1)
# print(data)
# print(type(data))

# file.close()

# file = open('sample.txt', 'a+')
# file.read()
# file.write('hello from python. \n after that numby test tabd')

# file.close()

# with open("demo.txt", "r") as file :
#     data = file.read()
# print(data)

# Deleting a file
# os module
# import os 
# os.remove('sample.txt')

# Practice


# with open('practice.txt', 'w') as file :
#     file.write('Hi everyone \n we are learning F/O \n using Java. \n i like programming in Java')

# with open('practice.txt', 'r') as file :
#     content = file.read()
#     data =  content.replace('Java','Python')
# with open('practice.txt', 'w') as file :
#     file.write(data)

# with open('practice.txt', 'r') as file :
#     filedata = file.read()
#     if (filedata.find('learning') != -1) :
#         print('Yes found')
#     else : 
#         print('Not found')

# def check_for_line():
#     with open('practice.txt', 'r') as file:
#         for line_no, line in enumerate(file, start=1):
#             if "a" in line:
#                 print(f"Found at line {line_no}")
#                 break

# check_for_line()

with open('practice.txt', 'r') as file : 
    filedata = file.read()
    count  = 0
    nums = filedata.split(',')
    for val in nums : 
        if int(val) % 2 == 0 :
            count += 1
            print('even')
        else : 
            print('odd')
print(count)