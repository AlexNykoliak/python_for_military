a = 'abcdefg'
b = [['Ivan'], ['Petro'], ['Stepan', 'Sofia']]


for i in a:
    print(i)

for i in b:
    for z in i:
        print(z)


for i in b:
    for z in i:
        if z == 'Sofia':
            print(f"Ім'я {z} є в списку {i}")


a = [[1, 2, 3, 4], [5, 6, 7, 8, 9]]

for number in a:
    for i in number:
        if i == 7:
            print('YES')

count = 0

while count < 10:
    print('Hello World')
    count += 1 #count = count + 1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in a:
    if i == 5:
        continue
    print(i)

for i in a:
    if i == 5:
        break
    print(i)

for i in a:
    if i == 5:
        pass
    print(i)

i = 1

while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


fruits = ["apple", "banana", "cherry"]

g = []

for x in fruits:
    x = x.upper()
    g.append(x)

print(g)


my_dict = {
    'name': 'Ivan',
    'age': 20,
    'city': 'Lviv',
}


for i in my_dict.items():
    print(i)

for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for key, value in my_dict.items():
    print(key, 'slkdmsoknmskdnm')


for x in range(1, 6, 2):
  print(x)


data = [i for i in range(1001) if i % 2 == 0]

print(data)


adj = ["red", "big", "tasty", 'small']
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


a = (1,2,3,4,5,'a',7,'o',8,9,10)


for i in a:
    if type(i) == str:
        print(a.index(i))

workers = ['Ivan', 'Denys', 'Roman', 'Ostap']

authenticated_workers = []


for worker in workers[:]:
    if worker not in authenticated_workers:
        authenticated_workers.append(worker)

print(authenticated_workers)


workers

a = workers
