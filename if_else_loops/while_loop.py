#Guess the number game
winning_num=7
guess_limit=3
guess_counter=0
while guess_counter<3:
    guess=int(input(f"enter your guess {guess_counter+1}:"))
    if winning_num==guess:
        print("You win, money money.....")
        break
    guess_counter +=1
else:
    print("kiki loseerrrrrrrrrrrr")