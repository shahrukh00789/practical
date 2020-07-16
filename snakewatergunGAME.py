import random
chances = 1
yourpoint=0
computerpoint =0
game =["snake","water","gun"]
print("<------------Snake Water Gun------------->")
print("Enter 's' for Snake,'w' for Water,'g' for 'GUN'")
while(chances<=10):
    yourturn=input()
    choice = random.choice(game)
    print(yourturn)
    if yourturn=="s" and choice=="gun":
        print("You lose a point")
        computerpoint=computerpoint+1
    elif yourturn =="s" and choice=="water":
        print("you earn a point")
        yourpoint=yourpoint+1
    elif yourturn=="s" and choice=="snake":
        print("you earn a point")
        yourpoint=yourpoint+1
    elif yourturn=="w" and choice=="snake":
        print("you lose a point")
        computerpoint=computerpoint+1
    elif yourturn=="w" and choice=="gun":
        print("you earn a point")
        yourpoint=yourpoint+1
    elif yourturn=="w" and choice=="water":
        print("you earn a point")
        yourpoint=yourpoint+1
    elif yourturn=="g" and choice=="gun":
        print("you earn a point")
        yourpoint=yourpoint+1
    elif yourturn=="g" and choice=="water":
        print("you lose a point")
        computerpoint=computerpoint+1
    elif yourturn=="g" and choice=="snake":
        print("you earn a point")
        yourpoint=yourpoint+1
    else:
        print("not proper selection")
    chances=chances+1

    print("you earn",yourpoint,"point")
    print("Computer earn",computerpoint,"point")
    # if computerpoint<=yourpoint:
    #     print("You Won")
    #


