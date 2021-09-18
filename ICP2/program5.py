#List comprehension

heightIninches = []                                     # creating empty list for height in inches and centimeter
heightIncentimeter = []
moreusers = 'Y'
while(moreusers == 'Y'):
    num = int(input("enter the list size "))      # get input from user how many heights need to be converted
    print("enter the heights of customers: ")
    for h in range (0,num):                                 # iterates for num times
        heightIninches.append(float(input()))

    heightIncentimeter=[height * 2.54 for height in heightIninches] # using list comprehension converting inches to centimeters

    print("height in inches is: {}" .format(heightIninches))
    print("height in centemeter is: {}" .format(heightIncentimeter))
    moreusers = input("Do you want to enter more? (Y/N): ")  # ask user if they want to check more number of heights



