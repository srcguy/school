list1 = []

def menu():
    option = int(input(">>"))
    if option == 1:
        calc()
    elif option == 2:
        adding_to_list()
    elif option == 3:
        substracting_from_list()
    else:
        print("Hm? Do you mean '1'?")
        menu()
        
def calc():
    x = int(input("Enter firts number: "))
    y = int(input("Enter second number: "))
    print(x, "+", y, "=", x+y)
    print(x, "-", y, "=", x-y)
    print(x, "*", y, "=", x*y)
    if (y != 0):
        print(x, "/", y, "=", x/y)
    else:
        print("We can't divide by zero ;)")
    menu()

def adding_to_list():
    z = int(input("Enter a number: "))
    a = int(input("How many time should I add this to list?: "))
    for i in range(a):
        list1.append(z)
    print(list1)
    menu()

def substracting_from_list():
    z = int(input("Enter a number of a number that I should delete: "))
    if z == 0:
        print("Nothing happened")
    else:
        list1.pop(z - 1)
    print(list1)
    menu()

menu()
