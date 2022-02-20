operation = input('''
Please choose the symbol corresponding to the math operation that you would like to complete
+ for addition
- for subtraction
* for multiplication
/ for division
''')


number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

#Addition
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

#Subtraction
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

#Multiplication
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

#Division
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Please choose a valid math operation before continuing')



input("Press [Enter] to exit the Calculator!")

