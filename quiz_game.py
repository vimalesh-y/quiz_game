print("Welcome to my game quiz!")

# Ask user if they want to play
playing = input("Do you want to play? ")

# Prompt Python to quit if answer is anything apart from "yes"
if playing.lower() != "yes":
    quit()

print("Ok! Let's start!")
score = 0

# Ask questions whilst addressing case-sensitivity using .lower()
answer = input("What does SDLC stand for? ")
if answer.lower() == "software development lifecycle":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does API stand for? ")
if answer.lower() == "application programming interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does IDE stand for? ")
if answer.lower() == "integrated development environment":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does UI stand for? ")
if answer.lower() == "user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 4 questions correct!")