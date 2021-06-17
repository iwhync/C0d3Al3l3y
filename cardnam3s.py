import re
import math
suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
x = input("input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
z = x.pop(0)
print(x)
for card in range(z):
    suit = math.trunc(x[card] / 13)
    rank = x[card] % 13
    print(f"{ranks[rank]}-of-{suits[suit]}")
