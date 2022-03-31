def grid(row, col):
    for i in range(1, row+1):
        value = i
        for j in range(1, col+1):
            if j == col:
                print(value, end ='')
            else:
                print(value, end = ', ')
            value += row
        print()


def print_grid():
    row = int(input("Enter number of rows: "))
    col = int(input("Enter number of columns: "))
    print("==================================================")
    grid(row, col)
    print("==================================================")

if __name__=="__main__":
  print_grid()