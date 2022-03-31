# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

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