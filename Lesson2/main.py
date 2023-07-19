a = 100

print(id(a) == id(100))

print(10/10)
print(10//10)
print(10*10)
print(10**10)

a = None

a = b = c = 10
c = 10
print(c + a)
a += 1
print(c + a)


a = 10

a = a + 10
a += 5

print(a)

print('hello' + str(2))

print('hello' == 'hello')

print(len('hello') == len('hello'))


a = 10
b = 10.5
c = 'hello'
d = True
e = None


my_tuple = (a, b, c, d, e)
my_set = {a, b, c, d, e}
my_dict = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e}

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(type(my_list))
print(len(my_list))

print(my_list[3:])
print(my_list[3:7])
print(my_list[::-1])
print(list(reversed(my_list)))

a = sorted(my_list, reverse=True)
print(a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(reversed(a)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

d = [1, 2, 1, 2, 3, 4, 3, 2, 1, 3, 4, 5, 4, 3, 2]

h = sorted(d, reverse=True)
print(h)

text = ['he', 'llo', 'wor', 'ld']
text = sorted(text)
print(text)


text = ['he', 'llo', 'wor', 'ld']
text = ''.join(text)
print(text)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.append(11)
print(a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.clear()
print(a)

a = [1, 2]
b = a

# print(a is b)
# print(a == b)

b = a.copy()
print(id(a))
print(id(b))


print(a.count(10))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [True]

a.extend([1, 1, 1, 1, 1, 1, 1])
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1]
b.extend(a)
# b = [True, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1]
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a.index(10))

a.insert(len(a), 100)
print(a)
a.append(101)
print(a)


v = [1, 2, 3]
v.insert(1, 'hello')  # після 1 індексу вставляємо 'hello'
print(v)

v.insert(len(v), 'world')  # після -1 індексу вставляємо 'world'
print(v)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = a.pop(0)

a.remove(10)
print(a)

a.reverse()

print(a)


def function():
    print('hello world')  # None


def function1():
    return 'Hello World'  # 'Hello World'


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.sort(reverse=True)
print(a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 2, 3, 4, [0]], True]

a[-2][-1][0].append(1)
a[-2][-1].append(1)

print(a)


a = [1, 2, 3, 4, 5, 'text', 'hello']
h = []

for i in a:
    if type(i) == str:
        h.append(i)

print(h)
