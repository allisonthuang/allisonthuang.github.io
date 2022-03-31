{% include navigation.html %}

# DS Project

#### [Link to Replit](https://replit.com/@allisonthuang/allisonthuanggithubio-1)

<iframe height="1000px" width="600px" src="https://replit.com/@allisonthuang/allisonthuanggithubio-1?lite=true#main.py"></iframe>

# Week 3 Snippets
#### Face fun
``` python
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
```

# Week 2 Snippets
#### Factorial
``` python
# factorial_class.py

class Factorial:
    def __init__(self):
        self.factorialSeq = [1,1]

  #__call__ is a special function in Python that, when implemented inside a class,
    # gives its instances (objects) the ability to behave like a function.
    # It means after implementing __call__ method inside the Python class,
    # we can invoke its instances like a function
    def __call__(self, n):
        if n < len(self.factorialSeq):
            return self.factorialSeq[n]
        else:
            # Compute the requested Factorial number
            factorial_number = n * self(n - 1)
            self.factorialSeq.append(factorial_number)
        return self.factorialSeq[n]

factor_of = Factorial() # object instantiation and run __init__ method
print(factor_of(5)) # object running __call__ method

def tester():
    # Make a factorial object
    while True:
        factorial_of = Factorial()
        n = input("Enter the number of terms: ")
        try:
            n = int(n)
            # Validate the value of n
            #The isinstance() function in Python returns true or false if a variable matches a
            # specified data type. isinstance(variable_to_check, data_type)
            if not (isinstance(n, int) and n >= 0):
                raise ValueError
            print("{0}! is: ".format(n))
            print(factorial_of(n)) # print the nth term
            print("Factorial sequence of 0 to {0} is: ".format(n))
            print([factorial_of(i) for i in range(0,n+1)])
            break
        except:
            print(f'Positive integer number expected, got "{n}" Try again.')

if __name__ == "__main__":
    tester()
```

#### Factors
``` python
def factors(n):
    factorsseq = []
    x = range(1, n + 1)
    for value in x:
        if (n % value == 0):
            factorsseq.append(value)
            print(value, end=' ')
    print(factorsseq)


class Factors:
    def _init_(self):
        self.factorsseq = []
      
    def _call_(self, n):
      for value in range(1, n + 1):
        if n % value == 0:
            self.factorsseq.append(value)
      return self.factorsseq
      
factors_of = Factors() # object instantiation and run _init_ method

def tester():
  print("Test factors of 69:")
  factors(69)
  print("Test factors of 420:")
  factors(420)
  
  try:
    n = int(input("What # for factors?: "))
    if not (isinstance(n, int) and n >= 0):
      raise ValueError
    print("The number {0}'s factors are': ".format(n))
    print(factors_of(n)) # print the nth term
  except:
    print(f'Invalid input: "{n}" Try again.')

if __name__ == "__main__":
    tester()
```

#### GCD
``` python
def igcd(a, b):
    if a > b:
        s = b
    if b > a:
        s = a
    for i in range(1, s + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd



class Gcd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        if self.a > self.b:
            s = self.b

        if self.b > self.a:
            s = self.a

        for i in range(1, s+1):
            if self.a % i == 0 and self.b % i == 0:
                gcd = i
        return gcd
print("This is OOP Form")      

def print_gcd():
    x = int(input("Enter a number: "))
    y = int(input("Enter a second number: "))
    print("==================================================")
    print("This is OOP Form")      
    f = Gcd(x,y)
    print("The GCD : ",end="")
    print(f())
    
    print("---------------------------------------------------")

    print("This is Imperative Form")
    print(igcd(x,y))

    print("==================================================")

if __name__=="__main__":
  print_gcd()
```

#### Palindrome
``` python
class Palindrome:
    def __call__(self, j):
        # Remove special characters from a string
        n = ''.join(filter(str.isalnum, j))
        n = n.lower()
        revn = n[::-1]
        if revn == n:
            self.result = (j + " is a palindrome.")
        else:
            self.result = (j + " is not a palindrome.")

        return self.result

palindrome_of = Palindrome()  # object instantiation and run __init__ method



def palindrome(j):
    # Remove special characters from a string and changes all letters to lowercase
    n = ''.join(filter(str.isalnum, j))
    n = n.lower()
    # reverses the string
    revn = n[::-1]
    # checks if the string is the same as the reversed string
    if revn == n:
        print(j + " is a palindrome.")
    else:
        print(j + " is not a palindrome.")


def tester():
    j = input("Enter a word: ")
    print(palindrome_of(j))  # print the nth term


if __name__ == "__main__":
    tester()
```

# Week 1 Snippets
#### Fibonacci
``` python
def recur_fibo(n): 
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# Fibonacci helper function that helps print
def fibo():
  nterms = int(input('Input a number:')) # Put number for input
  if nterms <= 0:
    print("Plese enter a positive integer")
  else:
    print("Your saucy sequence:")
    for i in range(nterms):
      print(recur_fibo(i))
```

#### Loops
``` python
InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Allison",  
               "LastName": "Huang",  
               "DOB": "July 27",  
               "Birthplace": "San Diego",  
               "Email": "allisontrhuang@gmail.com",  
               "Favorite_Hobbies":["Photography","Yearbook","Graphic Design","SD STEM Startups", "Hating Life"]  
              })  

InfoDb.append({  
               "FirstName": "Bria",  
               "LastName": "Gilliam",  
               "DOB": "September 27",  
               "Birthplace": "Los Angeles",  
               "Email": "briagee@gmail.com",  
               "Favorite_Hobbies":["A","B","C"], 
              })  


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"],
          InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Favorite Hobbies: ",
          end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(
        InfoDb[n]
        ["Favorite_Hobbies"]))  # join allows printing a string list with separator
    print()


# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop():
    n = int(input('What # do you want?:'))
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop():
    n = int(input('What # do you want now?'))
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# new method
def recursive_helper():
    recursive_loop()
    return

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)
    
def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
```

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
