x, y= 5, 11

# or

t = 5, 11
w, x = t 

print(w, x)

people = [("Tom", 42, "Mechancic"), ("James", 22, "Pilot")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person = ("Tom", 42, "Mechancic")
name, _, profession = person # _ used to ignore a specific variable

head, *tail = [1, 2, 3, 4]

