def digitsum(number):
    if number < 0:
        number = -number
    s = 0
    while number != 0:
        remainder = number % 10
        s += remainder 
        number = number // 10
    return s


def print_digitsum():
    x = int(input("Enter a number: "))
    print("==================================================")
    ans = digitsum(x)
    print('Digit sum:', ans)
    print("==================================================")

if __name__=="__main__":
  print_digitsum()