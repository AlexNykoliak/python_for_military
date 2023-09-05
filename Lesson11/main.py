# Hello students!


def function():
    print("This is a function inside a module")

def square(x):
    return x * x


def main():
    a = 100
    a = int(str(a) + str(a))
    return a


print(main())

a = []

def function(some_list):
    for i in some_list:
        if i % 2 == 0:
            a.append(i)

function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a)


def function1(some_list):
    return [i for i in some_list if i % 2 == 0]


print(function1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


a = [1,2,3,4,5]

b = [i for i in range(1,1000000) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0]

print(b)


from operator import le
import string

alphabet = string.ascii_lowercase

a = [i for i in alphabet if i not in "aeiou"]

o = []

for i in alphabet:
    if i not in "aeiou":
        o.append(i)


import string
import random

all_symbols = string.ascii_letters + string.digits + string.punctuation

def function(length):
    return "".join(random.sample(all_symbols, length))

def password_generator(length):
    return "".join(random.choices(all_symbols, k=length))

print(password_generator(10))

password = '#[1_E}R-Xx'

def hacker_password(length:int, some_string: str):
    variants = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
    count = 0
    for i in variants:
        for j in variants:
            for k in variants:
                for l in variants:
                    for m in variants:
                        for n in variants:
                            if i + j + k + l + m + n == some_string:
                                print('Password is hacked')
                            else:
                                print('Password is not hacked')
                                count += 1
                                print(count)

hacker_password(10, password)



def function():
    def function1():
        print("This is a function inside a function")
    return function1()

function()

data = {
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def function(a,b):
    return lambda x, y: x + y

a = lambda x, y: x + y


def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

print(sum(5))



def func(*args, **kwargs):
    print(args, kwargs)
    
    
func(1,2,3, a=1, b=2, c=3, d=4, e=5)


def function(name=None, age=None, country=None):
    print(f"Hello, {name}. You are {age} years old. You are from {country}")
    
    
function(age=29, country="Ukraine", name="Alex")
function()
