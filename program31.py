#Name: Shahriar M Alam
#Email: Shahriar.alam96@myhunter.cuny.edu
#Date: March 4, 2020
#This program prints: Turtle String

import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'B':
        tess.backward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == 'S':
        tess.shape("turtle")
    elif ch == 'D':
        tess.shape("dot")
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'r':          #turn red
        tess.color("red")
    elif ch == 'g':          #turn green
        tess.color("green")
    elif ch == 'b':          #turn blue
        tess.color("blue")
    elif ch == 'p': 
        tess.color("purple")
    else:                    #for any other character, print an error message
        print("Error: do not know the command:", ch)

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked
