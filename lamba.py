def multiply(x, y):
    return x * y

print(multiply(5, 4))

(lambda w, z: w * z)(5, 4)

def double(x):
    return x * 2

sequence = [2, 4, 5, 9]
double = [double(x) for x in sequence]
doubled = map(double, sequence)

# doubler = list(map(lamba x:x * 2, sequence))