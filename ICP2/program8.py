# printing string alternatives

def string_alternative():
    string1 = input("enter a string:")      # asking user to enter string
    print(string1[::2])                     # prints every alternative characters starting from the first character

if __name__ == "__main__":
   string_alternative()             # calling string_alternative function from main