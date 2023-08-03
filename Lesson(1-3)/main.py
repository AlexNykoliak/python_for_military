a = 10
b = 10.0
c = 'text'
d = True

f = 10.0
f = int(f)

int()
float()
str()
bool()

a = 10
print(a)

print(type(a))


a = 10

print(a != 10)
print(a == 10)


a = 10
b = 20

a = [1, 2, 3, 4, 5]

a.sort(reverse=True)
print(a)

a.append(6)
print(a)

a.insert(0, 0)
print(a)


f = a.pop(0)
print(f)

t = a.remove(5)


a = (1, 2, 1, 3, 2, 4, 5)

print(a.count(1))
print(a.index(2))

a = (1, 2, 1, 3, 2, 4, 5)

a = list(a)
a.pop(2)

a = tuple(a)
print(a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in a:
    print(i, end=',')


a = '12345678dfghjkl'

g = "-".join(a)
print(g)


myTuple = ("John", "Peter", "Vicky")

x = ", ".join(myTuple)

print(x)


for i in a:

    if i.isdigit():
        print(i)
        print('there were numbers')

    elif i.isalpha():
        print(i)
        print('there were letters')

if i == int(i):
    print(i, end=',')


a = {1,2,3,4,5, (1,2,3,4,5)}
print(type(a))


a = (1,2,3,4,5,6,7,8,9,10) #9109727825473806502
b = 1,2,3,4,5,6,7,8,9,10   #9109727825473806502


import time

start = time.time()
a = (i for i in range(1, 1000000) if i % 2 == 0)
for i in a:
    if i == 1000000:
        print(i)
end = time.time()
print(end - start)


# 0.06346893310546875 list 1 mln
# 0.05113363265991211 tuple 1 mln

# 6.355692386627197 list
# 5.584459066390991 tuple

a = 10.0

if type(a) == str:
    print('a is string')
elif type(a) == int:
    print('a is int')
elif type(a) == float:
    print('a is float')


a = [1,2,3,4,5,6,7,8,9,10, [1,2,3,4,5,6,7,8,9,10, [1,2,3,4,5,'Z',7,8,9,10]]]

a[-1][-1][5] = 'A'

print(a)

a = (1,2,3,4,5,6, [1,2,3])
a[-1].clear()
print(a)


a = [1,2,3,4,5,6,7,8,9,10]

b = []
for i in a:
    b.append(i)
print(b)

d = [i for i in range(1, 11)]
f = list(i for i in range(1, 11))

print(d)
print(f)


print(list(i for i in range(1, 11)))
print(list(i for i in range(1, 11, 2)))
print(list(i for i in range(11)))


import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

start = datetime.datetime.now()
timedelta = datetime.timedelta(days=1)
print(start + timedelta)


number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
operation = input('Enter operation: ')

if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)



# py - m venv venv
# venv\Scripts\activate

# Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUser
