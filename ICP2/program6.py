# using Nested loops
heightIninches = []                                             # creating empty list for height in inches and centimeter
heightInincentimeter = []
moreusers = 'Y'                                                 # set moreusers initially to 'y'

while(moreusers == 'Y'):
    num = int(input("enter the list size "))          # get input from user how many heights need to be converted
    print("enter the heights of customers")                    # get input of heights(it will be in inches)
    for h in range (0,num):
        heightIninches.append(float(input()))                   # iterates for num times
    for c in range (num):
        heightInincentimeter.append(heightIninches[c] * 2.54)   # converts from inches to centimeter by multiplying 2.54
    print("height in inches : {}".format(heightIninches))
    print("height in centimeter : {} ".format(heightInincentimeter))
    moreusers = input("Do you want to enter more? (Y/N): ")     # ask user if they want to check more number of heights


