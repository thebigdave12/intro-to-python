friends = ["rolf", "jenn", "tom"]

print("rolf" in friends)

coworkers = {"rolf", "jenn", "tom"} #could use to check to see if there is any duplicate or new friends

movies_watched = {"LOTR", "Ironman", "Titanic"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print(f"I've haven't watched {user_movie} too!")