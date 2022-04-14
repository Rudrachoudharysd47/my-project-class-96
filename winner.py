import random
x = random.randint(1,9)
chances = 5
while chances > 0 :
    guess = int(input("please guess a number between 1 and 9"))
    if x == guess:
        print("you won the game")
        break

    elif x>guess:
        print("your guess is too low")
    elif x<guess:
        print("your guess is to high")
    else:
        print("guess between 1 and 9")
    
    chances = chances-1

if not chances > 0:
    print("you lose the game! the number is " , x)