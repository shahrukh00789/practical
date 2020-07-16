class library():
    def __init__(self,atitle):
        self.title=atitle


    def navigationbar(self):
        print("1.ADD BOOK")
        print("2.SHOW BOOKS")
        print("3.RENDER BOOKS")
        print("4.RENTED BOOKS")

        choice = int(input("Enter 1 for add book 2 for show book 3 for render book 4 for rent book and any number for quit\n"))

        if choice == 1:
            welcome.addbook()
        elif choice == 2:
            welcome.showbook()
        elif choice == 3:
            welcome.renderbook()
        elif choice==4:
            welcome.showrenderbook()
        else :
            print("Thanks")

    def addbook(self):
        newbook=input("Enter Book which you wat to add\n")
        book.append(newbook)
        option=input("Do you want to see your added book in the list press y , n for no and r for rent and q for quit\n")
        if option=="y":
            welcome.showbook()
        elif option=="n":
            welcome.navigationbar()
        elif option =="r":
            welcome.renderbook()
        elif option=="q":
            exit()

    def showbook(self):
        for item in book:
            print(f"{item}")
        option = input("IF want to rent press 'r' ,for adding press 'a' for home press 'h'")
        if option == "r":
            welcome.renderbook()
        elif option=="h":
            welcome.navigationbar()
        elif option=="a":
            welcome.addbook()
        elif option=="q":
            exit()

    def renderbook(self):
        rent=input("Enter which book you want for rent")
        if rent in book:
            book.remove(rent)
            rendorbook.append(rent)
            print("Successfully rented")
        else:
            print("required book is not available kindly check for the other book")

        option = input("Do you want to see your Render book  in the list press y for Home press n and q for quit\n")
        if option == "y":
            welcome.showrenderbook()
        elif option=="n":
            welcome.navigationbar()
        elif option=="q":
            exit()

    def showrenderbook(self):
        for item in rendorbook:
            print(item)
        choice = int(input("Enter 1 for add book 2 for show book 3 for render book 4 for rent book and any number for quit\n"))

        if choice == 1:
            welcome.addbook()
        elif choice == 2:
            welcome.showbook()
        elif choice == 3:
            welcome.renderbook()
        elif choice=="q":
            exit()

book=["1.Machine Learning","2.Deep Learning","3.Artificial Intelligence","4.Artificial Neural network"]
rendorbook=[]
welcome=library("<-------------------Welcome To Shahrukh Library----------------------> ")
print(welcome.title)
welcome.navigationbar()


