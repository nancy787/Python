marks = int(input("Enter your marks"))
if(marks >= 90) :
    print('A')
elif(marks >= 80 and marks < 90) :
    print('B')
elif(marks >= 70 and marks < 80) :
    print('C')
else:
    print('D')

# programme to chek number is even or odd
num = int(input("Enter your number"))
if (num % 2) == 0 :
    print('Even')
else :
    print('Odd')

# programme to chek where teh the numbver is multiple of 7 or not
num = int(input("Enter number ")) 
if(num % 7) == 0 :
    print(True)
else :
    print(False)

# progrramme to find greatest of three number
n1 = int(input('Enter First Number'))
n2 = int(input('Enter Second Number'))
n3 = int(input('Enter Third Number'))

if(n1 > n2 and n1 > n3) :
    print(n1, "is greated")
elif(n2 > n1 and n2 > n3) :
    print(n2, 'is greater')
else :
    print(n3, 'is greater')