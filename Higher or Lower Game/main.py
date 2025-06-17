from game_data import data
from art import logo,vs
import random


game_over=False
score=0
i=random.randint(0,49)

while not game_over:

    j=random.randint(0,49)
    while j==i:
        j = random.randint(0, 49)


    print(logo)
    if score>0:
        print(f"You're right! Your score is {score}")
    print(f"\nCompare A: {data[i]['name']}, a {data[i]['description']}, from {data[i]['country']}\n")
    print(vs)
    print(f"\nCompare B: {data[j]['name']}, a {data[j]['description']}, from {data[j]['country']}\n")
    ans=input("Who has more followers? Type 'A' or 'B'").upper()

    if data[i]['follower_count']>data[j]['follower_count']:
        max="A"
    else:
        max = "B"

    if ans==max:
        i=j
        score+=1

    else:
        game_over=True

    print("\n" * 20)


print(logo)
print(f"Sorry that's wrong. Final score:{score}")



