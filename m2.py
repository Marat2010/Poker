import random

# Deck — колода, Suit — масть
# Hearts — червы, Diamonds — бубны
# Clubs — трефы, Spades — пики
# Jack — валет, Queen — дама, King — король, Ace — туз, Joker — джокер

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
numb = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

# suit = random.choice(suits)
# num = random.choice(numb)
# random_card = [suit, num]
# print(random_card)

deck = []
for s in suits:
    for n in numb:
        deck.append([s, n])

print(len(deck))

while str(input("Еще? (y-продолжить): ")) == 'y':
    i = 0
    stol = []
    while i < 5:
        random_card = random.choice(deck)
        deck.remove(random_card)
        stol.append(random_card)
        i += 1
    print(stol)
    print(deck)

from collections import Counter

Counter(random.choices(['Катя', 'Коля'], weights=[10, 20])[0]
    for _ in range(100000))

