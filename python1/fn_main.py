 practice questions:  

# 1 

def greet(name):
    print(f"Hello {name}")
greet("Ananda")

# 2

def sum(a , b):
    print(f"The sum of numbers {a} and {b} is: {a+b}")
sum(6 , 7)

# 3

def square(a):
    return f"the square of number {a} is {a*a}"
print(square(7))

# 4 

def checkeven_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

checkeven_odd(4)

# 5

def checklarge_num(a , b , c):
    if a > b and a > c:
        print(f"{a} is biggest betweeen three number {a} , {b} , {c}")
    elif b > a and b > c:
        print(f"{b} is biggest betweeen three number {a} , {b} , {c}")
    else:
        print(f"{c} is biggest betweeen three number {a} , {b} , {c}")
checklarge_num(4 , 5 , 6)

# 6

def len_str(str):
    count = 0
    for char in str:
        count += 1
    return count
name = "Ananda"
l = len_str(name)
print(f"The length of the string {name} is {l}")

# 7

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(7))

# another method....

def factorials(n):
    facts = 1
    for i in range(1 , n+1):
        facts *= i
    return facts
print(factorials(7))

# 8

def check_pnz(num):
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print("zero")

check_pnz(-9)


# 9

def sum1(list_num):
    total = 0
    for num in list_num:
        total += num
    return total
list = [4,5,6,7,8,9]
print(sum1(list))

# 10

def is_palindrome(num):
    n = str(num)
    if n == n[::-1]:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not palindrome")


is_palindrome(121)

# 11

def is_primenum(num):
    count = 0
    for i in range(1 , num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(f"The {num} is prime number")
    else:
        print(f"The {num} is not a prime number")

is_primenum(9)

# 12

def rev_str(s):
    return s[::-1]
str = "python"
print(rev_str(str))

# 13

def count_vowles(str):
    count = 0
    for char in str:
        if char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char == "U":
            count +=  1
    return count
    
c = count_vowles("programming")
print(c)

# 14
def min_max(list):
    minimum = list[0]
    maximum = list[0]
    for num in list:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return minimum , maximum

l = [4,2,7,3,5,9,5,6]
print(min_max(l))

# 15

def check_psswrdstrn(password):
   has_digit = "false"
   has_alpha = "false"
   for char in password:
        if char.isdigit():
            has_digit = "true"
        elif char.isalpha():
            has_alpha = "true"
        else:
            print("password is incorrect")


   if len(password) >= 8 and has_digit and has_alpha:
       print("password is correct")
   else:
       print("password is incorrect") 

check_psswrdstrn("Ananda1234")


