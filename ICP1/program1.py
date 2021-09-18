# input string python from console
def input_string():
    inputstring = input('enter input to display  : ')
    inputstring = inputstring[2:]  # deleting two characters from input string
    print(inputstring[::-1])    # reversing input string


input_string()
