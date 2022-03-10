"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- Stringy' )
    print('2 -- Numby' )
    print('3 -- Matrix' )
    print('4 -- Swap' )
    print('5 -- Exit' )
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Numby',
    3: 'Matrix',
    4: 'Swap',
    5: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def stringy():
    print('You chose \' 1 -  Stringy\'')

# menu option 2
def numby():
    print('You chose \' 2 - Numby\'')

# menu option 3
def matrix():
  matrixa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  matrixb = []
  matrix1(matrixa, matrixb)
  matrix2(matrixb)
  
def matrix1(matrixa, matrixb):
  for i in range(len(matrixa)):
      for j in range(len(matrixa[i])):
          matrixb.append(matrixa[i][j])
  return(matrixb)

def matrix2(matrixa, matrixb):
  print(matrixb[0], matrixb[1], matrixb[2])
  print(matrixb[3], matrixb[4], matrixb[5])
  print(matrixb[6], matrixb[7], matrixb[8])
  
# menu option 4
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

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-5: '))
            if option == 1:
                stringy()
            elif option == 2:
                numby()
            elif option == 3:
                matrix()
            elif option == 4:
                swap()
            # Exit menu    
            elif option == 5:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 5.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()