n=45

while(True):
    number = int(input("Enter The Number you have guessed between range of 1 to 100"))
    if number == n :
        print("You have Successfully guess the number")
        break
    elif number < n :
        print("Actual number is greater than your guessed number")
        continue
    elif number > n :
        print("Actual number is less than your guessed number")
        continue

