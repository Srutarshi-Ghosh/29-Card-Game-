import random

power = ['J', '9', 'A', '10', 'K', 'Q', '8', '7']
points = [3, 2, 1, 1, 0, 0, 0, 0]
cards = ["JS", "JH", "JC", "JD", "9S", "9H", "9C", "9D", "AS", "AH", "AC", "AD", "10S", "10H", "10C", "10D", "KS", "KH", "KC", "KD", "QS", "QH", "QC", "QD","8S", "8H", "8C", "8D","7S", "7H", "7C", "7D"]



def deal(c):
    c1 = c
    p = []
    temp = []
    for i in range(4):
        for j in range(4):
            x = random.choice(c1)
            c1.remove(x)
            temp.append(x)
        p.append(temp)
        temp.clear()

    return c1, p[0], p[1], p[2], p[3]


def bid():



def game():
    player = []
    opp1 = []
    partner = []
    opp2 = []
    c = cards
    c, player, opp1, partner, opp2 = deal(c)


