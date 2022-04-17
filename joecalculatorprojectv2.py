#I have created a function that runs the calculator called "calculation"
def greetings():
    print(''' 
Welcome to Joe's Calculator Program!
 _____________________
|  _________________  |
| | BY:JOE BELCHER  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|      ''')

#this message displays after the user chooses 'N' at the end screen
def exitCalc():
    print('Thank you for using my calculator!')

def calculation():
    operation = input('''
Please choose the symbol corresponding to the math operation that you would like to complete
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Enter your first integer: '))
    number_2 = int(input('Enter your second integer: '))

#Addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        result = int(number_1+number_2)
        i=1
        div=0
        while i<=result:
            if result%i==0:
                div = div +1
            i=i+1
        if div == 2:
            print('The answer is prime.')
        else:
            print('The answer is not prime.')


#Subtraction
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        result = int(number_1-number_2)
        if result > 0:
            i=1
            div=0
            while i<=result:
                if result%i==0:
                    div = div +1
                i=i+1
            if div == 2:
                print('The answer is prime.')
            else:
                print('The answer is not prime.')
        else:
            print('The answer is not positive and therefore cannot be prime.')
#Multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        result = int(number_1*number_2)
        i=1
        div=0
        while i<=result:
            if result%i==0:
                div = div +1
            i=i+1
        if div == 2:
            print('The answer is prime.')
        else:
            print('The answer is not prime.')
#Division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        result = int(number_1/number_2)
        if result == number_1/number_2:
            i=1
            div=0
            while i<=result:
                if result%i==0:
                    div = div +1
                i=i+1
            if div == 2:
                print('The answer is prime.')
            else:
                print('The answer is not prime.')
        else:
            print('The answer is not an integer and cannot be prime')
    else:
        print('Please choose a valid math operation before continuing')

    repeat()


#to run the calculation function again after its completion, we create a function called "repeat"
def repeat():

    repeat_calc = input(''' Would you like to run another calculation? Type Y for yes or N for no: ''')
    
    #We create an input for either answer and print either run another calculation or print a goodbye message
    
    if repeat_calc.upper() == 'Y':
        calculation()
    #the elif has the user press the Enter key to close the calculator program
    elif repeat_calc.upper() == 'N':
        exitCalc()
        input("Press [Enter] to exit the calculator")
    
    #if the user chooses neither option, we present a message saying to choose either Y or N
    else:
        repeat()
        
            
greetings()
calculation()
