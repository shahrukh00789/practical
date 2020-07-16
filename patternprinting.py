numberofrows = int(input("how many row you want to printed"))
boolean = bool(input("Enter 1 for true 0 for false"))

if boolean ==True:
    for i in range(1,numberofrows+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
elif boolean == False:
    for i in range(numberofrows,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()


