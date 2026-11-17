print("Greetings welcome to my python tutorial.")
print("I have 2 programs that i will present")
print("instead of putting print everyline ")
print("I'll tell instructions instead so read carefully")
print("first daclare A as a first number and B as second")
print("Second daclare them as float, because it's possible that they won't be a whole number.")
print("Third declare the opperator, and command their functions.")
print("use if, elif and else statements.")
print("if and elif are choices while else is where your choices are invalid")
print("make sure to type what the instructions says")
print("Not typing numbers won't give you an answer")


print("\n===SIMPLE CALCULATOR===")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
     print(a + b)
elif op == "-":
     print(a - b)
elif op == "*":
     print(a * b)
elif op == "/":
     print(a / b)
else:
    print("Invalid operator")
    print(f"Select only numbers{a and b} and operations{op}")    

print("\n===NUMBER GUESSING GAME===")

print("Now moving on to 2nd program")
print("it's called Number guessing game")
print("First stop is type import random")
print("And declare the lowest number which is the number 1")
print("After the declaring the lowest number which is 500")
print("type random.randint and the number range")
print("Because the program will pick the random number for you to guess which daclare as answer")
print("type guess so the game will tell how many are your attempts")
print("type is with underscore and running")
print("To command the program to run while the player is playing")
print("Declare it as also True and do not type False")
print("Next is print and f string for identation, to the lowest and highest number")
print("Type guess follow up by the equal sign, make sure it's input and not print")
print("In if condition type isadigit follow up with brackets, the program read this as a number")
print("And do not type isalpha, the program read that as a letter")
print("Type guess equal sign int as integer")
print("Command a hint after the if statement, game will tell you exaclty the hint and if you succeed")
print("After that now you can now type False, to stop the game after guessing")



import random

lowest_num = 1
highest_num = 500
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Guessing number game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number ONLY between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("That's too low try it again")
        elif guess > answer:
            print("That's too high try it again")
        else:
            print(f"PERFECT! the answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
        
    else:
        print("Invalid guess")
        print(f"Select a number ONLY between {lowest_num} and {highest_num}")

print("that's all")
print("Thank you")