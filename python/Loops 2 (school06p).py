n = int(input("How many times should i ask you for numbers?: "))#requests an integer from user.
for i in range(n):#execute 'n' times
    x = int(input("Enter firts number: "))#requests an integer from user. that number will be stored as 'x'
    y = int(input("Enter second number: "))#requests an integer from user. that number will be stored as 'y'
    print(x, "+", y, "=", x+y)#shows text and variables and some calculations#we need to use ',' to separate text from variables
