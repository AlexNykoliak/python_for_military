
# def letters_check(letter):
#     # count 'aouei'
#     y = letter.count('a') + letter.count('o') + letter.count('u') + letter.count('e') + letter.count('i')
#     print('Number of vowels: ', y)


# count = 0
# count_vowels = 0

# def letters_check(letter):
#     for i in letter:
#         if i.lower() in 'aouei':
#             global count
#             count += 1

#         elif i.lower() not in "aouei ,!":
#             global count_vowels
#             count_vowels += 1


# letters_check('Hello Folks, I am glad to see you!')

# print('Number of vowels: ', count, 'Number of consonants: ', count_vowels)

# import string


# def letters_check(letter):
#     for i in letter:
#         if i in string.ascii_letters and not i.lower() in 'aouei':
#             counter_consonants = letter.count(i)
#             print(f"Count of consonants: {counter_consonants}")

#         elif i.lower() in 'aouei':
#             counter_vowels = letter.count(i)
#             print(f"Count of vowels: {counter_vowels}")


# letters_check('Hello Folks, I am glad to see you!')


# class BankAccount:

#     def __init__(self, name, lastname, balance=0):
#         self.name = name
#         self.lastname = lastname
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return f"Your balance is: {self.balance}"


#     def withdraw(self, amount):
#         self.balance -= amount
#         return f"Your balance is: {self.balance}"


# sofia142627 = BankAccount('Sofia', 'Kachmar', 0)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def print_info(self):
#         return f"The name of the student {self.name}, the age of the student {self.age}"

#     def set_age(self, age):
#         self.age = age
#         return f"The age of the student {self.age}"

#     def set_name(self, name):
#         self.name = name
#         return f"The name of the student {self.name}"

#     def get_name(self):
#         return self.name


# oleksandr = Student('Alex', 28)

# print(oleksandr.print_info())
# print(oleksandr.set_age(30))


# class Car:
#     def __init__(self, engine, speed, diesel) -> None:
#         self.engine = engine
#         self.speed = speed
#         self.diesel = diesel

#     def print_info(self):
#         return f"Engine: {self.engine}, Speed: {self.speed}, Diesel: {self.diesel}"


# class ElectricCar(Car):

#     def __init__(self, engine, speed, diesel, battery):
#         super().__init__(engine, speed, diesel)
#         self.battery = battery

#     def print_info(self):
#         return f"Engine: {self.engine}, Speed: {self.speed}, Diesel: {self.diesel}, Battery: {self.battery}"


# class A:
#     def method(self):
#         print("A.method() called")

#     def methodmethodmethod(self):
#         print("A.methodmethodmethod() called")


# class B(A):
#     def method(self):
#         print("B.method() called")

#     def methodmethodmethod(self):
#         print("OK")

# b = B()
# b.methodmethodmethod()
