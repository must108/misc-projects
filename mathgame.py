import os 
import random as r
import sys
import time

score = 0

def mathProblem(inp):
    x = r.randint(1, 10)
    y = r.randint(1, 10)

    if(inp == "addition"):
        answer = x + y
        user = input(str(x) + "+" + str(y) + ": ")
    elif(inp == "subtract"):
        answer = x - y
        user = input(str(x) + '-' + str(y) + ": ")
    elif(inp == "multi"):
        answer = x * y
        user = input(str(x) + "*" + str(y) + ": ")

    if(user == str(answer)):
        print("Correct!")
        global score
        score += 1
        time.sleep(1)
        os.system("cls")
    elif(user == "exit"):
        os.system("cls")
        endSequence()
    else:
        print("Wrong!")
        time.sleep(1)
        os.system("cls")
        endSequence()

def exitMessage():
    print("Input 'exit' at any problem to end the game!")
    time.sleep(1)
    os.system("cls")

def endSequence():
    print("Your score was " + str(score) + "!")
    time.sleep(1)
    sys.exit()
 

print("Welcome to the Math Game!")
time.sleep(2)
os.system("cls")

type = input("Enter game type (addition, subtract, or multiplication): ")
os.system("cls")

if(type == 'addition'):
    exitMessage()
    while(1):
        mathProblem("addition")
elif(type == 'subtract'):
    exitMessage()
    while(1):
        mathProblem("subtract")
elif(type == 'multiplication'):
    exitMessage()
    while(1):
        mathProblem("multi")
else:
    print("input not valid!")
    sys.exit()