{% include navigation.html %}

# DS Project

#### [Link to Replit](https://replit.com/@allisonthuang/allisonthuanggithubio-1)

<iframe height="1000px" width="600px" src="https://replit.com/@allisonthuang/allisonthuanggithubio-1?lite=true#main.py"></iframe>

# Week 3 Snippets

# Week 2 Snippets

# Week 1 Snippets

# Week 0 Snippets
#### Swap
``` python
def swap():
  c = int(input('Whats your first number?:'))
  d = int(input('Whats your second number?:'))
  c,d = swap1(c,d)
  print(c,d) 

def swap1(a,b):
  if a > b:
    b, a = a, b  # swap values
  else:
    a, b = a, b
  return a, b  # return 2 values
```

#### Christmas Tree
``` python
def gen_tree(rows):
    # replace *s with a space in a rowsxrows matrix
    for i in range(0, rows+1):
        for j in range(0, rows-i):
            print(end=' ')
        for k in range(0, i):
            print('*', end=' ')
        print()


def driver():
    rows = int(input("Enter height of the tree:  "))
    gen_tree(rows)
    # single line lambda function
    # a is the parameter to the function
    # lambda function returns the value for # of spaces
    spaces = lambda a: int(a-2) + a % 2
    moveRt = " " * spaces(rows)
    # print the trunk of the tree
    for i in range(3):
        print(moveRt, end="###")
        print()
```

#### Ship
``` python
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)

# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    |\   ")
    print(sp + "    |/   ")
    print(SHIP_COLOR, end="")
    print(sp + "\__ |__/ ")
    print(sp + " \____/  ")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)
```

#### Matrix
``` python
def matrix():
  matrixa = [[input('1 number:'), input('2 number:'), input('3 number:')], 
             [input('4 number:'), input('5 number:'), input('6 number:')], 
             [input('7 number:'), input('8 number:'), input('9 number:')]]
  matrixb = []
  matrix1(matrixa, matrixb)
  print(matrixb)
  
def matrix1(matrixa, matrixb):
  for i in range(len(matrixa)):
      for j in range(len(matrixa[i])):
          matrixb.append(matrixa[i][j])
  return(matrixb)

def matrix2(matrixa, matrixb):
  print(matrixb[0], matrixb[1], matrixb[2])
  print(matrixb[3], matrixb[4], matrixb[5])
  print(matrixb[6], matrixb[7], matrixb[8])
```
