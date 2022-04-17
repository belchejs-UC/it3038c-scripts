I created a simple to use multi-function calcualtor based off of the program found at https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3

My program uses a set of initial functions chosen by the user
<pre><code>
    def calculation():
     operation = input('''
    Please choose the symbol corresponding to the math operation that you would like to complete
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
</code></pre>
You then input two different numbers

<pre><code>
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    
  </code></pre>
The program then runs a function that takes the mathematical operation chose by the user and the earlier numerical inputs to determine your answer. 

<pre><code>  
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
 </code></pre>
 Within my operations code, there is a check for whether the integer for the result is either prime or not prime
  <pre><code>
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
    </code></pre>
    
 The program then asks the user if they would like to repeat the process and leaves them with a kind message if they choose to close the program. 

    repeat_calc = input(''' Would you like to run another calculation? Type Y for yes or N for no: ''')

    #We create an input for either answer and print either run another calculation or print a goodbye message
  <pre><code>
    if repeat_calc.upper() == 'Y':
        calculation()
    #the elif has the user press the Enter key to close the calculator program
    elif repeat_calc.upper() == 'N':
        exitCalc()
        input("Press [Enter] to exit the calculator")

    #if the user chooses neither option, we present a message saying to choose either Y or N
    else:
        repeat()
   </code></pre>    
   Pleae leave any questions or comments on my Github! ^_^
