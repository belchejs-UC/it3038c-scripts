#This line starts the program and has the user enter their age in years (eg. 22, 57,)
Age = int(input('Please enter your age in years: '))

#this line uses multiplication to convert days all the way to seconds
seconds = Age * (365*24*60*60)

#output of seconds
print("Your age in seconds is: " +str(seconds))
#output at end of program, prevents it from closing automatically
input("Press [Enter] to exit the Years-to-Seconds Calculator!")
