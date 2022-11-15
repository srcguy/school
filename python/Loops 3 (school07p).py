n = int(input("How many times should i ask you for numbers?: "))
while n > 0:#while 'n' is bigger than zero, then...
    x = int(input("Enter firts number: "))#requests an integer from user. that number will be stored as 'x'
    y = int(input("Enter second number: "))#requests an integer from user. that number will be stored as 'y'
    print(x, "+", y, "=", x+y)#shows text and variables and some calculations#we need to use ',' to separate text from variables
    n = n - 1#substract one from 'n'#for example, if 'n' was equal to '3', now 'n' equals '2'