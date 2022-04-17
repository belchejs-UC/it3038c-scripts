I created a simple to use multi-function calcualtor based off of the program found at https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3
I decided to add some features to the project such as making sure the calculator loops back to asking the user to enter a new calculation, providing information on if the answer is prime, and letting the user end the program when they are finished using it. I also added some fun ASCII art of a calculator! 

My program uses a set of initial functions chosen by the user

    def calculation():
     operation = input('''
    Please choose the symbol corresponding to the math operation that you would like to complete
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

You then input two different numbers

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    
The program then runs a function that takes the mathematical operation chose by the user and the earlier numerical inputs to determine your answer. 
       
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

    repeat()
    
 The program then asks the user if they would like to repeat the process and leaves them with a kind message if they choose to close the program. 

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
        
   Pleae leave any questions or comments on my Github! ^_^

