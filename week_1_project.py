import random

guesses=['rock','paper','scissors']
rounds=5
my_score=0
bot_score=0

for round in range(1, rounds+1):
    print(f"Round{round}")
    my_guess=input("Choose(rock, paper or scissors):").lower()

    if my_guess not in guesses:
       print("invalid choice!")
    computer_guess=random.choice(guesses)

    if my_guess==computer_guess:
        print("Tie!")

    elif(
        (my_guess=='rock'and computer_guess=='scissors')or (my_guess=="paper" and computer_guess=="rock") or
        (my_guess=='scissors' and computer_guess=="paper")
    ):
        print("Your point!")
        my_score+=1

    else:
        print("Bots point!")
        bot_score+=1

    if my_score==3 or bot_score==3:
        break

    print(f"Me :{my_score  Bot{bot_score}}")

    if my_score>bot_score:
        print("You win!")
    elif bot_score>my_score:
        print("Bot wins")
    else:
        print("Tie!")
        