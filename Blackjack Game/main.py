from art import logo
import random

def blackjack():

        playing=True

        while playing:

            wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if wanna_play == "y":

                print("\n"*20)
                print(logo)

                cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                user=[]
                comp=[]

                for i in range(2):
                    user.append(random.choice(cards))
                    comp.append(random.choice(cards))

                user_sum=sum(user)
                comp_sum=sum(comp)

                another_card="y"

                while another_card=="y" and user_sum<21:
                    print(f"Your cards: {user}, current sum: {user_sum}\n")
                    print(f"Computer's first card: {comp[0]}")
                    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

                    if another_card=="y":
                        user.append(random.choice(cards))
                        user_sum = (sum(user))


                while comp_sum<17:
                    comp.append(random.choice(cards))
                    comp_sum = (sum(comp))

                if 11 in comp and comp_sum>21:
                    cards.remove(11)
                    cards.append(1)


                print(f"Your final hand: {user}, final score: {user_sum}")
                print(f"Computer's final hand: {comp}, final score:{comp_sum}")

                if user_sum>21 and comp_sum>21:
                    print("It's a push. You and dealer both went over. ")
                elif user_sum>21:
                    print("You lose. You went over.")
                elif comp_sum>21:
                    print("You win! Dealer went over!")
                else:
                    if user_sum==21:
                        print("You win with a Blackjack!")
                    elif user_sum>comp_sum:
                        print("You win!")
                    elif user_sum==comp_sum:
                        print("It's a draw!")
                    elif comp_sum==21:
                        print("You lose! Dealer has blackjack.")
                    else:
                        print("You lose!")
            else:
                playing=False



blackjack()