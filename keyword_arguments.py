# def named(name, age):
#     print(name, age)


# details = {"name": "Bob", "age": 25}

# named(**details)

def named(*kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.item():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=33)