from math import *

age = int(input("Enter the child's age: "))
height = float(input("Enter the child's height: "))
weight = int(input("Enter the child's weight: "))

result = (
    "He can enter the amusement park"
    if ((age > 14 or height >= 1.60) and weight < 50)
    else "He can not enter the amusement park"
)

print(result)


speed = int(input("Enter speed: "))
time = int(input("Enter time: "))

distance = speed * time
print(f"distance traveled: {distance}m/s")

firstNote = float(input("Enter your first note: "))
secondNote = float(input("Enter your second note: "))
thirdNote = float(input("Enter your third note: "))

print("Your average is: ", (firstNote + secondNote + thirdNote) / 3)

answerCorrect = int(input("Enter number of correct answers: "))
answerIncorrect = int(input("enter number of incorrect answers: "))
answerBlank = int(input("Enter number of blank answers: "))

print("Your score is: ", answerCorrect * 3 + answerIncorrect * -1 + answerBlank * 0)

gamesWon = int(input("Enter number of games won: "))
gamesLossed = int(input("enter number of games lossed: "))
gamesTied = int(input("Enter number of tied games: "))

print("Your score is: ", gamesWon * 3 + gamesLossed * 1 + gamesTied * 0)


result = 3**0.75 * sqrt(2) / (exp(2) - 1)
print(f"Result: ", result)

a = sqrt(40)
d = a * sqrt(2)
print(f"Result: ", round(d, 2))
