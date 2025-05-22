class Card(object):
    """A Blackjack card."""
    pass

c = Card()
c.face = "Ace"
c.suit = "Spades"
c.value = 11

print(type(c))

def hand_value(hand):
    value = 0
    for card in hand:
        value += card.value
    return value

def card_string(card):
    article = "a "
    if card.face in [8, "Ace"]:
        article = "an "
    return article + str(card.face) + " of " + card.suit

print(card_string(c))