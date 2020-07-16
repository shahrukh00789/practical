print("<-------------------------Health Management System----------------------------->")
def showdata(clientname,inputplan):
        if clientname =="Irfan" and inputplan =="Diet":
                f=open("irfandiet.txt")
                content = f.read()
                print(content)
        elif clientname == "Sam" and inputplan == "Diet":
                f = open("irfandiet.txt")
                content = f.read()
                print(content)
        elif clientname == "Shahrukh" and inputplan == "Diet":
                f = open("irfandiet.txt")
                content = f.read()
                print(content)
        elif clientname == "Irfan" and inputplan == "Exercise":
                f = open("IrfanExercise.txt")
                content = f.read()
                print(content)
        elif clientname == "Shahrukh" and inputplan == "Exercise":
                f = open("ShahrukhExercise.txt")
                content = f.read()
                print(content)
        elif clientname == "Sam" and inputplan == "Exercise":
                f = open("SamExercise.txt")
                content = f.read()
                print(content)
        else:
                print("Not Proper Entry")

        print("Do you Want To Show More data enter 'y' for yes 'n' for no")
        again = input()
        if again == "y":
                template()
        else:
                print("Bye Bye Bye")


def entryofdata(clientname,inputplan):
        if clientname =="Irfan" and inputplan =="Diet":
                 dietdetails = input("Enter Diet details")
                 f= open("Irfandiet.txt","a")
                 f.write(dietdetails)
                 f.close()
        elif clientname =="Sam" and inputplan =="Diet":
                dietdetails = input("Enter Diet details")
                f = open("Samdiet.txt", "a")
                f.write(dietdetails)
                f.close()
        elif clientname =="Shahrukh" and inputplan =="Diet":
                dietdetails = input("Enter Diet details")
                f = open("Shahrukhdiet.txt", "a")
                f.write(dietdetails)
                f.close()
        elif clientname =="Sam" and inputplan =="Exercise":
                Exercisedetails = input("Enter Exercise details")
                f = open("SamExercise.txt", "a")
                f.write(Exercisedetails)
                f.close()
        elif clientname =="Shahrukh" and inputplan =="Exercise":
                Exercisedetails = input("Enter Exercise details")
                f = open("ShahrukhExercise.txt", "a")
                f.write(Exercisedetails)
                f.close()

        elif clientname =="Irfan" and inputplan =="Exercise":
                Exercisedetails = input("Enter Exercise details")
                f = open("IrfanExercise.txt", "a")
                f.write(Exercisedetails)
                f.close()
        else:
                print("Kindly check proper value")
        print("Succefully Entry Done ."
              "Do you want to add more details enter 'y' for yes 'n' for NO")
        again =input()
        if again =="y":
                template()

def template():
        print("Client Name")
        client =["Irfan","Sam","Shahrukh"]
        plan =["Diet","Exercise"]
        print(client)
        print("Enter 'Entry' for Entry Details and 'Show' For the Showing details")
        choice =input()
        clientname =input("Enter Client Name For which you want to Enter the record\n")
        print(plan)
        inputplan =input("Enter For which you want to Enter the record\n")

        if choice == "Entry":
                entryofdata(clientname, inputplan)
        elif choice == "Show":
                showdata(clientname,inputplan)

template()
