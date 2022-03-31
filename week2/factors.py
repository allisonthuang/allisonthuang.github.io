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