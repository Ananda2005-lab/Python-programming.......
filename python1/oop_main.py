 practice question....

# 1

class car:
    def __init__(self , brand , speed):
        self.brand = brand
        self.speed = speed
    def show(self):
        print(f"The car brand name is {self.brand}")
        print(f"The car {self.brand} highest speed is {self.speed}")

c2 = car("audi" , 250)
c2.show()

# 2

class student:
    def __init__(self , name , marks):
        self.name = name 
        self.marks = marks
    def grade(self):
        if self.marks >= 60:
            print(f"{self.name} is pass.His mark is {self.marks} ")
        else:
            print(f"{self.name} is fail.His mark is {self.marks} ")

s1 = student("Ananda" , 89)
s1.grade()
s2 = student("rahul" , 40)
s2.grade()

# 3

class mobile:
    def __init__(self , company , price):
        self.company = company
        self.price = price

    def discount(self):
        price = self.price * 0.1 # discount 10%
        new_price = self.price - price 
        print(f"The discount price of {self.company} mobile is {new_price}")
m1 = mobile("samsung" , 50000)
m1.discount()


# 4

class BankAccount:
    def __init__(self , name , Balance):
        self.name = name 
        self.Balance = Balance

    def deposite(self , amount1):
        self.amount1 = amount1
        self.Balance = self.Balance + self.amount1
        print(f"The deposite amount are {self.amount1}")
        print(f"After deposite {self.amount1} then the total balance is {self.Balance}")
    
    def withdrawl(self , amount2):
        self.amount2 = amount2
        self.Balance = self.Balance - self.amount2
        print(f"The withdrawl amount are {self.amount2} then total balance is {self.Balance}")
    
b1 = BankAccount("SBI"  , 100000)
b1.deposite(50000)
b1.withdrawl(35000)

# 5(inheritance)

class Animal:
    def __init__(self , name):
        self.name = name 
    def sound(self):
        print("Animal makes sound") 

class Dog(Animal):
    def __init__(self, name , breed):
        super().__init__(name)
        self.breed = breed
    def show(self):
        print(self.name)
        print(self.breed)

a1 = Dog("Tomy" , "Rotwailer")
a1.show()
a1.sound()


# 6

class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

class Employee(person):
    def __init__(self, name, age , salary):
        super().__init__(name, age)
        self.salary = salary
    def show(self):
        print(f"The Employee name is: {self.name}")
        print(f"The Employee age is: {self.age}")
        print(f"The Employee salary is: {self.salary}")

E1 = Employee("Ananda" , 20 , 18000)
E1.show()



# 7

class vehicle:
    def __init__(self , brand):
        self.brand = brand
class car(vehicle):
    def __init__(self, brand , speed):
        super().__init__(brand)
        self.speed = speed

    def info(self):
        print(f"The car brand name is {self.brand}")
        print(f"The car highest speed is {self.speed}")
c1 = car("XUV 7xo" , 250)
c1.info()

# 8

class BankAccount:
    def __init__(self , balance):
        self.balance = balance

class SavingAccount(BankAccount):
    def __init__(self, balance , interest):
        super().__init__(balance)
        self.interest = interest
    def store(self):
        print(f"BAlANCE: {self.balance}")
        print(f"INTEREST: {self.interest}")

A1 = SavingAccount(100000 , "6%")        
A1.store()


# 9 

class Teacher:
    def __init__(self , name):
        self.name = name
class MathTeacher(Teacher):
    def __init__(self, name , Subject):
        super().__init__(name) 
        self.Subject = Subject
    def show(self):
        print(f"Teacher name is {self.name}")
        print(f"His subject is {self.Subject}")

T1 = MathTeacher("Ananda" , "Mathematics")
T1.show()


# MINI PROJECT (OOP).....


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class SavingAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)

    def show(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

a1 = SavingAccount("Ananda", 10000)

a1.deposit(5000)
a1.withdraw(3000)
a1.show()



