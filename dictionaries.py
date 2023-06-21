friend_ages = {"Rolf": 24, "Adam": 30}

friend_ages["Adam"] #would equal 30

friend_ages["Rolfee"] = 22 # would add rolf to the friend set


friends = [
    {"name": "Rolf", "age": 30},
    {"name": "Tom", "age": 33},
]

print(friends[1]["name"]) #will print Tom

for name, age in friend_ages.items():
    print(f"{name} is {age} years old")