 practice questions....(if else condition)
# 1


num = int(input("Enter a num "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 2

num = int(input("Enter a Number "))

if num % 2 == 0:
    print( num , " is Even")
else:
    print( num , "is Odd")

# 3

age = int(input("Enter your Age "))

if age >= 18:
    print("Eligible for Vote")
else:
    print("Not Eligible for Vote")    

# 4

User_num1 = int(input("Enter a number "))
User_num2 = int(input("Enter a number "))

if User_num1 > User_num2 : 
    print(User_num1 ,  " is greater than ", User_num2)
else:
    print(User_num2 ,  " is greater than ", User_num1)

# 5

num = int(input("Enter a Number "))

if num % 5 == 0 :
    print(num , "is divisble by 5")
else :
    print(num , "is not divisible by 5")


# 6

year = int(input("Enter  a year: "))

if (year % 4 == 0 and year % 100 != 0)or year % 400 == 0:
    print(year , "year is a leap year")
else:
    print(year , "year is not a leap year")

# 7

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 > num2 and num1 > num3:
    print(num1 , " is largest number")
elif num2 > num1 and num2 > num3:
    print(num2 , " is largest number")
else:
    print(num3 , " is largest number")

# 8

char = "u"

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print(char , ' is vowel')
else:
    print(char , ' is a consonant')

# 9

marks = int(input('Enter your marks: '))

if marks <= 100  and marks >= 90:
    print("grade = A")
elif marks <= 89 and marks >= 75:
    print("grade = B")
elif marks <= 74 and marks >= 50:
    print("grade = C")
elif marks < 50 :
    print("grade = D OR Fail" )
else:
    print("Invaild Marks")


# 10

num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    print(num , " is a three digit number")
else:
    print(num , " is not a three digit number")

# 11

Age = int(input("Enter your Age: "))

if Age < 13:
    print("child")
elif Age >= 13 and Age <= 19:
    print("Teen")
else:
    print("Adult")

# 12

t_sidesA = int(input("Enter triangle sides: "))
t_sidesB = int(input("Enter triangle sides: "))
t_sidesC = int(input("Enter triangle sides: "))

if (t_sidesA + t_sidesB) > t_sidesC and (t_sidesA + t_sidesC) > t_sidesB and (t_sidesB + t_sidesC) > t_sidesA:
    print("valid triangle")
else:
    print("invalid triangle")

# 13

num = 3
count = 0

for i in range(1 , num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print(num , " is a prime number")
else:
    print(num , " is not a prime number") 

# 14

char = input("Enter a keyboard character: ")

if char >= "A" and char <= "Z":
    print("Character is in Uppercase")
elif char >= 'a'  and char <= "z":
    print("character is in Lowercase")
elif char >= "0" and char <= "9":
    print("character is in Digit")
else:
    print("character is in special character")

# 15 

username = input("Enter your username: ")
password = input("Enter your password: ")

if username != "admin":
    print("Invalid username")
elif password != "1234":
    print("wrong password")
else:
    print("login successful")


