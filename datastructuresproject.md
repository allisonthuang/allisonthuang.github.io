{% include navigation.html %}

# Data Structures Project

### Repl Links

{% include replit_embed.html %}

[TT0 - Python Menu](https://replit.com/@allisonthuang/allisonthuang-AllisonCSPTri3#.replit)

### Code Snippets
### Menu
```# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()

import tt0_1
import tt1

main_menu = [
    ["Swap", tt0_1.swap],
    ["Matrix", tt0_1.matrix],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Ship Animation", tt0_1.ship],
    ["Face", tt0_1.face],
    ["Christmas Tree", tt0_1.tree],
    ["Better Christmas Tree", tt0_1.driver],
]

list_sub_menu = [
    ["For loop", tt1.for_loop],
    ["While Loop", tt1.while_loop],
    ["Recursive Looop", tt1.recursive_loop],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def list_submenuc
# using list_sub_menu list:
# list_submenuc works similarly to menuc
def list_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, list_sub_menu)
    m.menu()


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", submenu])
    menu_list.append(["List", list_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def list_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, list_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()```

### Swap
```
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

### Animations
```
# menu option 1
def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def face_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + " ( ͡❛ ͜ʖ ͡❛) ")
    print(sp + "  /| |\  ")
    print(sp + "   ||  ")
    print(sp + "  _||_ ")
    print(SHIP_COLOR, end="")
    print(RESET_COLOR)


# ship function, iterface into this file
def face():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        face_print(position)  # call to function with parameter
        time.sleep(.1)

# menu option 2
def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def tree_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    *    ")
    print(SHIP_COLOR, end="")
    print(sp + "   ***   ")
    print(sp + "  *****  ")
    print(sp + " ******* ")
    print(sp + "*********")
    print(sp + "   | |   ")
    print(RESET_COLOR)


# ship function, iterface into this file
def tree():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        tree_print(position)  # call to function with parameter
        time.sleep(3.5)

# Function to print("Tree Pattern") - Better tree
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

      
# original ship print code
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

### Matrix
```
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
