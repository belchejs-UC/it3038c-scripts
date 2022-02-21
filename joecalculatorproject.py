operation = input('''
Please choose the symbol corresponding to the math operation that you would like to complete
1 for addition
2 for subtraction
3 for multiplication
4 for division
''')

#
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

#Addition Operator 
if operation == '1':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

#Subtraction Operator
elif operation == '2':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

#Multiplication Operator
elif operation == '3':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

#Division Operator
elif operation == '4':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

#If the user does not choose a valid operator, this message appears before the app closes  
else:
    print('Please choose a valid math operation before continuing')



input("Press [Enter] to exit the Calculator!")

