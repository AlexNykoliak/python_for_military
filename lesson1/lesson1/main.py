print("Hello world!")
print('10 + 10')
print("10 + 10")
print(10+10)
print(10-10)
print(10*10)
print(10**10)
print(10/10)
print(10//10)


a = 10
print(id(a))
a = 100
print(10 + a)


a = b = c = d = 10

b = 20

print(b)

print(a)
print(id(a))
print(id(10))

print(id(a) == id(b))

a = 10
b = 10
c = 10

print(id(a))
print(id(b))
print(id(c))

print(id(a) == id(b) == id(c))


a = 10  # int, ціле число
b = 10.5  # float, дробове число
c = 'hello'  # str, рядок
d = True    # bool, булеве значення
e = False   # bool, булеве значення
f = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


print(10 < 10)

print(True > False)
print(1 > 0)

a = 10
a = float(a)

print(a)
print(type(a))
a = str(a)
print(a)

print(type(a))


int()
float()
str()
bool()


a = 10
b = "10"
# b = int(b)
# print(a + int(b))
print(a, b)


print("My name is Oleksandr", "I am 28 years old", sep="*****")


name = "Oleksandr"
age = 28

print(f"Hello, my name is {name}, my age is {age}")

print("My name is Oleksandr", "I am", age, "years old")


text = "OLEKSANDR"
print(text.capitalize())
print(text.lower())


name = " Oleksandr "

# name = name.replace("O", "o")
name = name.strip
print(name)


text = 'abcdefg'
print(text[1])
