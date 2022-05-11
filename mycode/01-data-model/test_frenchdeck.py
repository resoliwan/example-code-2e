import collections

Card = collections.namedtuple("Card", ["suit", "number"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.cards = [
            Card(suit=suit, number=n) for n in self.ranks for suit in self.suits
        ]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[i]


def test_hello():
    deck = FrenchDeck()
    assert deck[0].suit == "spades"
    assert len(deck) == (13 * 4)
