mylist = [6, 7, 8, 9, 9]#creates list
print(mylist)#shows list
n = 0#sets 'n' to zero
for i in range(6):#execute six times...
    mylist.pop(0)#deletes first element of list
    mylist.append(n)#adds 'n' to the end og list
    print(mylist)#shows list
    n = n + 1#adds one to 'n'
