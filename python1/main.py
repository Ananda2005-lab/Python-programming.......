 # instance  , static , class method .....


class Employee:
    company = "HP"

    def __init__(self , name , salary):
        self.name  = name 
        self.salary = salary
        print(self.name)
        print(self.salary)


    @staticmethod
    def show(a , b):
        print(a + b)
   
    @classmethod
    def print_class(cls):
        return cls.company


    @classmethod
    def change_class(cls , new_name):
        cls.company = new_name
        return cls.company


e1 = Employee("Ananda" , 354687)

e1.show(2, 5)
e1.print_class()
e1.change_class("samsung")
print(e1.print_class())


# Magic(Dunder) Method....

class method:
    def __init__(self , name , age , a ):
        self.name = name
        self.age = age
        self.a = a
 

    def __str__(self):
        return f"My name is {self.name} , and my age is {self.age}"
    def __repr__(self):
        return f"name: {self.name}\nage: {self.age}"
    def __len__(self):
        return len(self.name)
    
    def __add__(self , others):
        return self.a + others.a
    

        

m1 = method("Ananda" , 20 ,  5)
m2 = method("Ananda" , 20 ,  8)
print(str(m1))
print(repr(m1))
print(len(m1))
print(m1 + m2)



# Error handling....
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))   
    print(a+b)

except Exception as e:
    print(e)


     
try:
   x = 10/2
except ZeroDivisionError as e:
   print("Error:" ,  e)

else:
   print("success")
finally:
   print("Always runs")


# map , filter , reduce method.....


#****

def square(x):
    return x * x

nums = [4 , 5 , 6 , 7 , 8 ,2]
sq = list(map(square , nums))
print(sq)

# ****

try:
    
   def convert_upercase(str):
      return str.upper()

   names = ["ram" , "shyam" , "mohan"]
   upper = list(map(convert_upercase , names))
   print(upper)

except:
   print("error")


# ****

def find_bignum(num):
   return num > 20



nums = [10,15,20,25,30]

bignum = list(filter(find_bignum , nums))
print(bignum)



# ****

def find_oddnum(num):
   return num % 2 != 0



nums = [1, 2, 3, 4, 5, 6]

oddnum = list(filter(find_oddnum , nums))
print(oddnum)


# ****

from functools import reduce


def bignums(a , b):
   if a > b:
      return a
   else:
      return b


nums = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

fb = reduce(bignums , nums)
print(fb)


# ****

nums = [1, 2, 3, 4, 5, 6]

def Evennum(n):
   return n % 2 == 0

evnum = list(filter(Evennum , nums))

print(evnum)

squre = list(map(lambda X: X*X , evnum))
print(squre)
