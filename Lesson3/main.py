
a = [1,2,3,4,5,6,7,8,9,10]

print(a[0])
print(a[1])
print(a[3:9])
print(a[::-1])
import time

print(list(range(1, 10, 2)))
a = list(range(10))     # 0~9
a = sorted(a, reverse=True)
print(a)

a = a[::-1]
print(a)

a = a.reverse()
print(a)


a = [1,2,3]

b = a.pop(0)

print(a)
print(b)


my_list = [1,2,3,4,5, True, 'Ivan']

my_tuple = (1,2,3, 'Ivan', [1,2,3,4,5,6,7,8,9,10, [True]], (1,2,3,4,5,6,7,8,9,10))

r = my_tuple[0:5]
print(r)

print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index('Ivan'))

print(my_tuple[4][10][0])

a = 10
a = float(a)
print(a)

print(type(my_tuple))
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple.pop(-1)
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)


h = (1,2,3,4,5,6,7,8,9,10, [1,2,3,4,[1,2,3,4,5,6,7,8,9,10, [1,2,3,4,5,6,7,8,9,10]]])

h[-1].pop(-1)
print(h)


import time

start = time.time()
my_list = [i for i in range(1000000) if i % 2 == 0]
end = time.time()
print(end - start) # 0.038234710693359375

start = time.time()
my_tuple = (i for i in range(1000000) if i % 2 == 0)
end = time.time()
print((end - start)*1000) # 0.010251998901367188


b = (1,2,3,4,5,6,7,8,9,10)
9109727825473806502 #hash

140308811440832 #id
print(id(b))


a = 10
print(hash(a))

b = ('Text') # 10
print(type(b))

a = 1000
b = (10,)
print(hash(a) == hash(b)) False

c = (1000)

print(hash(a) == hash(c))
print(id(a) == id(c))


a = 10
print(10 == 11)

a = [1,2,3,4,5,6,7,8,9,10]

print(a[0])
print(a[1])
print(a[3:9])
print(a[::-1])
import time

print(list(range(1, 10, 2)))
a = list(range(10))     # 0~9
a = sorted(a, reverse=True)
print(a)

a = a[::-1]
print(a)

a = a.reverse()
print(a)


a = [1,2,3]

b = a.pop(0)

print(a)
print(b)


my_list = [1,2,3,4,5, True, 'Ivan']

my_tuple = (1,2,3, 'Ivan', [1,2,3,4,5,6,7,8,9,10, [True]], (1,2,3,4,5,6,7,8,9,10))

r = my_tuple[0:5]
print(r)

print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index('Ivan'))

print(my_tuple[4][10][0])

a = 10
a = float(a)
print(a)

print(type(my_tuple))
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple.pop(-1)
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)


h = (1,2,3,4,5,6,7,8,9,10, [1,2,3,4,[1,2,3,4,5,6,7,8,9,10, [1,2,3,4,5,6,7,8,9,10]]])

h[-1].pop(-1)
print(h)


import time

start = time.time()
my_list = [i for i in range(1000000) if i % 2 == 0]
end = time.time()
print(end - start) # 0.038234710693359375

start = time.time()
my_tuple = (i for i in range(1000000) if i % 2 == 0)
end = time.time()
print((end - start)*1000) # 0.010251998901367188


b = (1,2,3,4,5,6,7,8,9,10)
9109727825473806502 #hash

140308811440832 #id
print(id(b))


a = 10
print(hash(a))

b = ('Text') # 10
print(type(b))

a = 1000
b = (10,)
print(hash(a) == hash(b)) False

c = (1000)

print(hash(a) == hash(c))
print(id(a) == id(c))


a = 10
print(10 == 11)


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

empty_list = []

for number in list_of_numbers:
    if number % 2 == 0:
        empty_list.append(number)


prof_list = [number for number in list_of_numbers if number % 2 == 0]

print(prof_list)


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

empty_list = []

for number in list_of_numbers:
    if number % 2 == 0:
        empty_list.append(number)


prof_list = [number for number in list_of_numbers if number % 2 == 0]

print(prof_list)


a = [1,2,3,4,5,6,7,8,9,10] # ordered, mutable, iterable
b = (1,2,3,4,5,6,7,8,9,10) # ordered, immutable, iterable

c = {1,2,3,4,5,6,7,8,9,10} # unordered, mutable, iterable, unique

c = {1,2,3,4,4,3,3,3,3,2,3,4,3,2,3}

a = set([1,2,3,4,4,3,3,3,3,2,3,4,3,2,3])
print(a)


print(c)
print(type(c))

a = ['Ivan', 'Maria', 'Stepan', 'Petro', 'Stepan']

a = list(set(a))
print(a)

b = {1,10,3,4,5,7,8,6,9}
print(b)

a = {1,2,3,(1,2,3)}
print(a)


a = [1,2,True, 3,4,5,6,7,8,9,10] # ordered, mutable, iterable

for i in a:
    print(i)


a = iter(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
