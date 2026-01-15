getters and setters...

class Account:
    def __init__(self, balance):
        self._balance = balance   # real variable

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid balance")


a = Account(10000)
print(a.balance)

a.balance = -5000     # Invalid
print(a.balance)

a.balance = 5000
print(a.balance)


# practice Questions....

# 1

class student:
    def __init__(self  , marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self , marks):
        if marks > 100 or marks < 0:
            print("Inavaild marks")

        else:
            self._marks = marks


s1 = student(98)
print(s1.marks)

s1.marks = 101
print(s1.marks)

s1.marks = 80
print(s1.marks)

# 2

class Employee:
    def __init__(self , salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self , salary):
        if salary < 0:
            print("invaild salary")
        else:
            self._salary = salary

E1 = Employee(100000)

print(E1.salary)

E1.salary = 50000
print(E1.salary)

E1.salary = -9000
print(E1.salary)
