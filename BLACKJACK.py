import random
import time


def blackjack(money, bet):

    deck = list("23456789AKJQ" * 4)
    deck.extend(["10", "10", "10", "10"])
    random.shuffle(deck)
    flag, p_ace, d_ace = 0, 0, 0
    split = False
    points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    dealer = []
    player = []
    player_score, dealer_score = [], []

    for i in range(2):
        player.append(deck.pop())
        player_score.append(points[player[i]])
        if player[-1] == "A":
            p_ace += 1
    for i in range(2):
        dealer.append(deck.pop())
        dealer_score.append(points[dealer[i]])
        if dealer[-1] == 'A':
            d_ace += 1

    print("Score of dealer is", points[dealer[0]], ". Cards : [ {} , X ]\n".format(dealer[0]))
    print("Your score is", sum(player_score), ". Cards : [ ", end="")
    print(*player, sep=" , ", end=" ]\n")

    if sum(dealer_score) == 21:

        print("Your score is", sum(player_score), ". Cards : [ ", end="")
        print(*player, sep=" , ", end=" ]\n")
        if sum(player_score) == 21:
            print("\n          BLACKJACK!!             \n")

        print("\nDealer's score is", sum(dealer_score), ". Cards : [ ", end="")
        print(*dealer, sep=" , ", end=" ]\n")

        if sum(player_score) == 21:
            print("\n          BLACKJACK!!             \n")
            print("\n          PUSH            \n It's a TIE !!")
            return bet

        else:
            print("You LOSE the Game !!")
            return 0

    if player[0] == player[1]:
        while True:
            s = input("Do you want to split(Yes/No): ")
            if s.upper() == "YES":
                if money >= bet:
                    split = True
                    break
                else:
                    print("You don't have enough money to SPLIT !!")
                    break
            elif s.upper() == "NO":
                break
            else:
                print("Invalid Input !!")

    if not split:
        while sum(player_score) < 21:
            s = input("Do you want to Hit or Stand: ")
            if s.upper() == "HIT":
                player.append(deck.pop())
                player_score.append(points[player[-1]])

                if sum(player_score) > 21 and p_ace > 0:
                    player_score[player_score.index(11)] = 1
                    p_ace -= 1

                print("Your score is", sum(player_score), ". Cards : [ ", end="")
                print(*player, sep=" , ", end=" ]\n")

                if sum(player_score) == 21:
                    print("\n          BLACKJACK!!             \n")

                if sum(player_score) > 21:
                    flag = 1
                    print("\n          BUST            \n")

            elif s.upper() == "STAND":
                print("\n\nYour score is", sum(player_score), ". Cards : [ ", end="")
                print(*player, sep=" , ", end=" ]\n")
                break

            else:
                print("Invalid Input!!")

        print("\n\nDealer's score is", sum(dealer_score), ". Cards : [ ", end="")
        print(*dealer, sep=" , ", end=" ]\n")
        if flag == 1:
            print("You LOSE the Game !!")
            return 0
        else:
            while sum(dealer_score) < 17:
                time.sleep(1.3)
                dealer.append(deck.pop())
                dealer_score.append(points[dealer[-1]])

                if sum(dealer_score) > 21 and d_ace > 0:
                    dealer_score[dealer_score.index(11)] = 1
                    d_ace -= 1

                print("Dealer's score is", sum(dealer_score), ". Cards : [ ", end="")
                print(*dealer, sep=" , ", end=" ]\n")

            if sum(dealer_score) == 21:
                print("\n          BLACKJACK!!             \n")

            if sum(dealer_score) > 21:
                print("\n          BUST            \n")
                print("You WIN the game !!!")
                return 2 * bet

            elif sum(player_score) == sum(dealer_score):
                print("\n          PUSH            \n It's a TIE !!")
                return bet

            elif sum(player_score) > sum(dealer_score):
                print("You WIN the Game !!!")
                return 2 * bet

            elif sum(dealer_score) > sum(player_score):
                print("You LOSE the Game !!")
                return 0

    else:

        hand1, hand2 = [], []
        h1, h2 = "", ""
        hand1.append(player[0])
        hand2.append(player[1])
        hand1_score, hand2_score = [player_score[0]], [player_score[1]]
        if 'A' in hand1:
            p_ace = 1
        else:
            p_ace = 0
        print("Hand 1 score: ", sum(hand1_score), ". Cards : [ ", end="")
        print(*hand1, sep=" , ", end=" ]")
        print("     Hand 2 score: ", sum(hand2_score), ". Cards : [ ", end="")
        print(*hand2, sep=" , ", end=" ]\n")

        print("\n\nHand 1 score: ", sum(hand1_score), ". Cards : [ ", end="")
        print(*hand1, sep=" , ", end=" ]\n")

        while sum(hand1_score) < 21:
            s = input("Do you want to Hit or Stand: ")
            if s.upper() == "HIT":
                hand1.append(deck.pop())
                hand1_score.append(points[hand1[-1]])
                if hand1[-1] == 'A':
                    p_ace += 1

                if sum(hand1_score) > 21 and p_ace > 0:
                    hand1_score[hand1_score.index(11)] = 1
                    p_ace -= 1

                print("Your Hand 1 score is", sum(hand1_score), ". Cards : [ ", end="")
                print(*hand1, sep=" , ", end=" ]\n")

                if sum(hand1_score) == 21:
                    print("\n          BLACKJACK!!             \n")

                if sum(hand1_score) > 21:
                    h1 = "(BUST)"
                    print("\n          BUST            \n")

            elif s.upper() == "STAND":
                print("\n\nYour Hand 1 score is", sum(hand1_score), ". Cards : [ ", end="")
                print(*hand1, sep=" , ", end=" ]\n")
                break

            else:
                print("Invalid Input!!")

        print("\n\nHand 2 score: ", sum(hand2_score), ". Cards : [ ", end="")
        print(*hand2, sep=" , ", end=" ]\n")
        if 'A' in hand2:
            p_ace = 1
        else:
            p_ace = 0

        while sum(hand2_score) < 21:
            s = input("Do you want to Hit or Stand: ")
            if s.upper() == "HIT":
                hand2.append(deck.pop())
                hand2_score.append(points[hand2[-1]])
                if hand2[-1] == 'A':
                    p_ace += 1

                if sum(hand2_score) > 21 and p_ace > 0:
                    hand2_score[hand2_score.index(11)] = 1
                    p_ace -= 1

                print("Your Hand 2 score is", sum(hand2_score), ". Cards : [ ", end="")
                print(*hand2, sep=" , ", end=" ]\n")

                if sum(hand2_score) == 21:
                    print("\n          BLACKJACK!!             \n")

                if sum(hand2_score) > 21:
                    h2 = "(BUST)"
                    print("\n          BUST            \n")

            elif s.upper() == "STAND":
                print("\n\nYour Hand 2 score is", sum(hand2_score), ". Cards : [ ", end="")
                print(*hand2, sep=" , ", end=" ]\n")
                break

            else:
                print("Invalid Input!!")

        print("\n\nHand 1 score: {}{}".format(sum(hand1_score), h1), "     Hand 2 score: {}{}".format(sum(hand2_score), h2))

        if h1 != "" and h2 != "":

            print("\n\nDealer's score is", sum(dealer_score), ". Cards : [ ", end="")
            print(*dealer, sep=" , ", end=" ]\n")
            print("You LOSE both hands !!!")
            return -bet

        else:

            print("\n\nDealer's score is", sum(dealer_score), ". Cards : [ ", end="")
            print(*dealer, sep=" , ", end=" ]\n")
            while sum(dealer_score) < 17:
                time.sleep(1.3)
                dealer.append(deck.pop())
                dealer_score.append(points[dealer[-1]])

                if sum(dealer_score) > 21 and d_ace > 0:
                    dealer_score[dealer_score.index(11)] = 1
                    d_ace -= 1

                print("Dealer's score is", sum(dealer_score), ". Cards : [ ", end="")
                print(*dealer, sep=" , ", end=" ]\n")

            if sum(dealer_score) > 21:
                print("\n          BUST            \n")
                if hand1 != "" and hand2 == "":
                    print("Hand 1: {}(BUST)        Hand 2: {}(WIN)".format(sum(hand1_score), sum(hand2_score)))
                    print("You WON one hand !!!")
                    return bet
                elif hand2 != "" and hand1 == "":
                    print("Hand 1: {}(WIN)        Hand 2: {}(BUST)".format(sum(hand1_score), sum(hand2_score)))
                    print("You WON one hand !!!")
                    return bet

            elif h1 == "" and h2 == "":
                a, b = "", ""
                if sum(dealer_score) > sum(hand1_score):
                    a = "LOSE"
                if sum(dealer_score) < sum(hand1_score):
                    a = "WIN"
                if sum(dealer_score) == sum(hand1_score):
                    a = "PUSH"

                if sum(dealer_score) > sum(hand2_score):
                    b = "LOSE"
                if sum(dealer_score) < sum(hand2_score):
                    b = "WIN"
                if sum(dealer_score) == sum(hand2_score):
                    b = "PUSH"

                print("\n\nHand 1: {}({})         Hand 2: {}({})".format(sum(hand1_score), a, sum(hand2_score), b))

                if a == "WIN" and b == "WIN":
                    return 3 * bet
                if (a == "PUSH" and b == "WIN") or (a == "WIN" and b == "PUSH"):
                    return 2 * bet
                if (a == "LOSE" and b == "WIN") or (a == "WIN" and b == "LOSE") or (a == "PUSH" and b == "PUSH"):
                    return bet
                if (a == "LOSE" and b == "PUSH") or (a == "PUSH" and b == "LOSE"):
                    return 0
                if a == "LOSE" and b == "LOSE":
                    return -bet

            elif h1 != "" or h2 != "":
                if h1 != "":
                    b = ""
                    if sum(dealer_score) > sum(hand2_score):
                        b = "LOSE"
                    if sum(dealer_score) < sum(hand2_score):
                        b = "WIN"
                    if sum(dealer_score) == sum(hand2_score):
                        b = "PUSH"

                    print("\n\nHand 1: {}{}         Hand 2: {}({})".format(sum(hand1_score), h1, sum(hand2_score), b))

                    if b == "LOSE":
                        return -bet
                    elif b == "WIN":
                        return bet
                    else:
                        return 0

                elif h2 != "":
                    a = ""
                    if sum(dealer_score) > sum(hand1_score):
                        a = "LOSE"
                    if sum(dealer_score) < sum(hand1_score):
                        a = "WIN"
                    if sum(dealer_score) == sum(hand1_score):
                        a = "PUSH"

                    print("\n\nHand 1: {}({})         Hand 2: {}{}".format(sum(hand1_score), a, sum(hand2_score), h2))

                    if a == "LOSE":
                        return -bet
                    elif a == "WIN":
                        return bet
                    else:
                        return 0


money = 500
print("       WELCOME TO PLAY BLACKJACK\n")
print("You Have $500 to Play!!")
while money > 20:
    while True:
        try:
            bet = int(input("Place your bet: $"))
            if bet > money:
                print("You Don't have enough money !!")
            elif bet < 20:
                print("Minimum amount for placing a bet is $20")
            else:
                break
        except Exception:
            print("Invalid Input !!")

    money -= bet
    money += blackjack(money, bet)
    print("\nYour Current Amount is: $" + str(money))

    if money < 20:
        print("Not enough to BET !!")
        print("Thanks for Playing ")
        break
