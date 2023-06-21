def multiply(*args):
    print(args)
    for arg in args:
        total = total * arg

multiply(1, 3, 5)


def add(x, y):
    return x + y
nums = [3, 5]
print(add(*nums))