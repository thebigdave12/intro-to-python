numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

friends = ["Tio", "Tom", "Tammie", "dave", "Ash"]
starts_t = [friend for friend in friends if friend.startswith("T")]

print(starts_t)