def calculator():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    operation = input("Enter operation: ")

    data = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    result = data[operation](number1, number2)
    print(result)


calculator()


# a = lambda x, y: x + y
# print(a(1, 2))
