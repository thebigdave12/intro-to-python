# number = 7

# while True:
#     user_input = input("Would you like to play guess a number (Y/n): ")

#     if user_input == "n": 
#         break

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("you guess right")
#     elif number - user_number in (1, -1):
#         print("You were off by one.")
#     else:
#         print("you guessed wrong")

#     user_input = input("Would you like to play guess a number (Y/n): ")


friends = ["Tom", "Jack", "Dave"]

for friend in friends:
    print(f"{friend} is my friend.")

for friend in range(3):
    print(f"{friend} is my friend.")
