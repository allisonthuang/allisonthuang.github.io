# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input

# Initial first attempt
"""def fibonacci():
  while True:
        try: 
          if n <= 1:
            print('Invalid option. Please enter a number greater than or equal to 0.')
            exit()
          else:
            return(fibonacci(n-1) + fibonacci(n-2))
        except ValueError: print('Invalid input. Please enter an integer input.')"""

# Actual fibonacci function
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