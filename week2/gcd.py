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