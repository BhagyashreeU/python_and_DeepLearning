# perform 4 operation on number provided by user
def operations():
    print('enter two numbers to perform arithmetic operations  : ')
    # reading two numbers from console
    num1 = int(input('enter number to perform operation: '))
    num2 = int(input('enter another number: '))

    # performing four arithmetic operations
    print('addition of two number :')
    print(num1 + num2)
    print('subtraction of two number :')
    print(num1 - num2)
    print('multiplication of two number :')
    print(num1 * num2)
    print('division of two number :')
    print(num1 / num2)

operations()


