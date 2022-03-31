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
