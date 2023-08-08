
# a = [1, 2, 3]
# b = (1, 2, 3)
# c = {1, 2, 3}


# my_dict = {
#     'name': 'Ivan',
#     'age': 20,
#     'is_student': True,
#     'skills': ['python', 'js', 'html', 'css'],
# }

# print(my_dict['name'])
# print(my_dict['age'])
# print(my_dict['is_student'])


# name = my_dict.get('name')
# print(name)
# name = my_dict['name']
# print(name)

# print(my_dict.get('skills'))

# my_dict['skills'] = ['python', 'js', 'html', 'css', 'django', 'flask', 'sql', 'git']

# print(my_dict)

# my_dict = {
#     'name': 'Ivan',
#     'age': 20,
#     'age': 40,
#     'is_student': True,
#     ('skills'): ['python', 'js', 'html', 'css', 'django', 'flask', 'sql', 'git', ['a', 'b', 'c', True]],
# }


# print(my_dict[('skills',)])

# print(my_dict)


# c = {
#     'name': 'Ivan',
#     'age': 20,
#     'classmates': {
#         'test_key': {
#                      'test_key1': 'test_value1'
#                      },
# }}

# print(c.get('name'))
# print(c.get('age'))
# print(c.get('classmates'))


# c['classmates']['test_key']['test_key1'] = '1000'

# print(c)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 2020
# }

# print(thisdict.keys())
# print(thisdict.values())

# int()
# float()
# str()
# list()
# tuple()
# set()
# dict()


# a = { 1: '1'}
# print(a)

# a = dict( p = 100)

# thisdict = dict(name = 'Alex')

# print(thisdict)

# import string

# alphabet = string.ascii_lowercase
# print(alphabet)

# a = { key: value for key, value in zip(range(1, 27), alphabet)}
# print(a)

# j = {
#     'name': 'Ivan',
# }

# data = {key: value for key, value in zip('A', 'B')}
# print(data)

# a = [1,2]
# b = ['a', 'b', 'c']

# print(tuple(zip([1,2,3], [-1,-2,-3])))


# a = {
#     'name': 'Ivan',
# }

# a['surname'] = 'Shevchenko'
# print(a)

# print(a.get('name'))
# print(a.get('surname'))


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)


# data = {
#     'name': 'Ivan',
#     'age': 20,
#     'is_student': True,
# }


# for key in data.keys():
#     print(key)

# for values in data.values():
#     print(values)

# for key, value in data.items():
#     print(key, value)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# mydict = thisdict.copy()
# print(mydict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011,
#     "city": "Kyiv"
#   }
# }


# myfamily["child3"]["city"] = "Lviv"

# print(myfamily)


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)


# x = ('key1', 'key2', 'key3')
# y = None

# thisdict = dict.fromkeys(x, y)

# print(thisdict)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
# }

# x = car.setdefault("lastname", "нема такого")

# print(x)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car.update({"color": "White"})

# print(car)


# import speech_recognition as sr
# import pyttsx3


# def main():
#     # Initialize recognizer
#     r = sr.Recognizer()

#     engine = pyttsx3.init()

#     # Capture audio from the microphone
#     with sr.Microphone() as source:
#         print("Please say something...")
#         audio = r.listen(source)
#         print("Recognizing...")

#         print("You said: " + r.recognize_google(audio))

#         spoken_text = r.recognize_google(audio)
#         engine.say(spoken_text)

#         engine.runAndWait()


# if __name__ == "__main__":
#     main()


# engine = pyttsx3.init()

# engine.say('10+10')

# engine.runAndWait()
