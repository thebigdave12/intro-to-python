number = 7
user_input = input("Would you like to play guess a number (y or n): ").lower()

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("you guess right")
    elif number - user_number in (1, -1):
        print("You were off by one.")
    else:
        print("you guessed wrong")

