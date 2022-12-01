"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

casper = turtle.Turtle()

# for c in ['red', 'green', 'blue', 'yellow']:
#     t.color(c)
#     t.forward(75)
#     t.left(90)

# Create a list of colors, called newColors
newColors = ["red", "yellow", "green"]

# Create a variable called index to access newColors
index = 0
print(newColors[index])

index = 1
print(newColors[index])

index = 2
print(newColors[index])

# Now let's print with a for loop
for index in range(3):
  print(newColors[index])

# Create a function that takes a turtle name and a color and draws a triangle
def triangle(turtleName, lineColor):
  turtleName.color(lineColor)
  for index in range(3):
    turtleName.forward(50)
    turtleName.left(120)

def square(turtleName, lineColor):
  turtleName.color(lineColor)
  for index in range(4):
    turtleName.forward(50)
    turtleName.left(90)

casper.speed('fastest')

casper.up()
casper.setpos(-80,0)
casper.down()

index = 0
for t in range(35):
  # print ('The value of index is: ' + str(index))
  triangle(casper, newColors[index])
  index = index + 1
  casper.left(10)
  if (index > 2):
    index = 0

casper.up()
casper.setpos(80,0)
casper.down()

index = 0
for t in range(35):
  # print ('The value of index is: ' + str(index))
  square(casper, newColors[index])
  index = index + 1
  casper.left(10)
  if (index > 2):
    index = 0

