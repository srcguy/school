x = int(input("Enter firts number: "))#requests an integer from user. that number will be stored as 'x'
y = int(input("Enter second number: "))#requests an integer from user. that number will be stored as 'y'
print(x, "+", y, "=", x+y)#shows text and variables and some calculations#we need to use ',' to separate text from variables
print(x, "-", y, "=", x-y)#shows text and variables and some calculations#we need to use ',' to separate text from variables
print(x, "*", y, "=", x*y)#shows text and variables and some calculations#we need to use ',' to separate text from variables
if (y != 0):#if (in Polish 'jeżeli') 'y' is not a zero (!=) then...
    print(x, "/", y, "=", x/y)#shows text and variables and some calculations#we need to use ',' to separate text from variables
else:#else...#in Polish 'w przeciwnym wypadku'
    print("We can't divide by zero ;)")#shows text