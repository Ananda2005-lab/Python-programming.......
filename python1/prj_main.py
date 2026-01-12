# miniproject 1(SMS)student management system

class person:
    def __init__(self , name):
        self.name = name 

class student(person):
    def __init__(self, name , roll , marks):
        super().__init__(name)
        self.roll = roll 
        self.marks = marks
    
    def result(self):
        if self.marks >= 40:
            print(f"{self.name} is pass")
        else:
            print(f"{self.name} is fail")

    def show(self):
        print(f"student name: {self.name}")
        print(f"student roll-no: {self.roll}")
        print(f"marks: {self.marks}")

s1 = student("Ananda" , 1 , 89)
s1.show()
s1.result()



# miniproject 2 (SBS)simple Bank system....


class Account:
    def __init__(self , name , balance):
        self.name = name 
        self.balance = balance

    def show_balance(self):
        print(f"Account Holder name: {self.name}")
        print(f"BALANCE: {self.balance}")

class SavingAccount(Account):
    
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def deposite(self , amount1):
        self.balance += amount1
        print(f"Deposited: {amount1}")


    def Withdrawl(self , amount2):
        self.balance -= amount2
        if self.balance >= amount2:
            print(f"withdrawn: {amount2}")
        else:
            print(f"Insufficient Balance")

A1 = SavingAccount("Ananda" , 100000)
A1.show_balance()
A1.deposite(32000)
A1.Withdrawl(45000)
A1.show_balance()
