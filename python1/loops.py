
# loops...
# practice questions....

# 1

for i in range(1 , 21):
    if i % 2 == 0:
        print(i)

# 2

for i in range(1 , 50):
    if i % 2 != 0:
        print(i)


# 3

for i in range (1 , 11):
    print(11-i)

# 4

word = "python"

for char in word:
    print(char)

# 5

for i in range(1 ,11):
    print(i*i)

# 6

for i in range(1 ,31):
    if i % 3 == 0:
        print(i)

# 7

sum = 0

for i in range(1,101):
    sum += i 
print(sum)

# 8

count = 0

for i in range(1 ,101):
    if i % 5 == 0:
        count += 1

print(count)
# 9

str = "education"

for char in str:
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        print(char)

# 10

str = "education"
rev_str = ""
for char in str:
    rev_str = char + rev_str
for char in rev_str:
    print(char)

# 11

for i in range(1 , 51):
    if i % 5 != 0:
        print(i)

# 12

sum = 0
for i in range(1 , 51):
    if i % 2 == 0:
        sum += i
print("The sum of first fifty number is " , sum)

# 13

for i in range(1 , 6):
    print("*" * i)

# 14

s = "" 
for i in range(1, 6):
    s = s + str(i)
    print(s)

# 15

num = 5

for i in range(1 , 6):
    print(str(num) * i)
    num -= 1
