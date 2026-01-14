# Decorators....


def decorators(func):
    def wrapper():
        print("WelCome")
        func()
        print("ThankYou")
    return wrapper()



@decorators
def say_Hello():
    print("Hello")


def my_decorators(role):
    def outer(func):
        def wrapper():
            print(f"Role: {role}")
            func()
        return wrapper    
    return outer

@my_decorators("Admin")
def Dashboard():
    print("Dashboard open")

    
@my_decorators("User")
def profile():
    print("Profile open")

Dashboard()
profile()


# 1

def my_decorators(func):
    def wrapper():
        print("start the function")
        func()
        print("End the function")
    return wrapper

@my_decorators
def function():
    print("Function execution is starting....")

function()

# 2 

def decorators(func):
    def wrapper():
        print("Hello")
        func()
        print("Bye")
    return wrapper

@decorators
def greet():
    print("Ananda")

greet()


# 3

logged_in = True

def login_required(func):
    def wrapper():
        if not logged_in:
            print("login required")
        else:
            func()

    return wrapper()            


@login_required
def dashboard():
    print("welocome to Dashboard")


# 4

def role_check(role):
    def decorators(func):
        def wrapper():
            print(f"role: {role}")
            func()
        return wrapper
    return decorators


@role_check("Admin")
def dashboard():
    print("Dashboard open")


dashboard()



# 5 



import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time Taken: {end - start}")
    return wrapper


@ timer
def long_task():
    for i in range (1 , 1000000):
        pass

long_task()

# 6


def my_decorators(n):
    def outer(func):
        def wrapper():
            for i in range (1 , n+1):
                func()

        return wrapper
    return outer

@ my_decorators(5)
def hello():
    print("Hello")

hello()

