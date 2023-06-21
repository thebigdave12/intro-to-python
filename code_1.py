x = 1500 # integer 
price = 9.99 # float

discount = 0.2

result = price * (1 - discount)

print(result) #console.log function 

name = "Rolf" # string

print(name)

greeting = f"Hello, {name}" #like template literal

print(greeting)

name_2 = "Bob"
greeting_2 = "Hello, {}"
with_name = greeting_2.format(name_2) #creating a template

print(with_name)

name_3 = input("Enter your name: ") # asking user for name

print(name_3)

size_input = input("How big is your house in square feet: ") 
square_feet = int(size_input) #changing str to an int

#.2f how many floats you want
