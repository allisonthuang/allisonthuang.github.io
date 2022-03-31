def pyramid(height):
    for i in range(1, height):
        # print space
        for j in range(0, height-i):
            print(' ', end='')
        # print *
        for j in range(2*i -1):
            print('*', end ='')
        
        print()

def print_pyramid():
    x = int(input("Enter number of rows: "))
    print("==================================================")
    pyramid(x)
    print("==================================================")

if __name__=="__main__":
  print_pyramid()