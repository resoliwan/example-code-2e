import collections

Card = collections.namedtuple("Card", ["suit", "rank"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.cards = [
            Card(suit=suit, rank=n) for n in self.ranks for suit in self.suits
        ]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[i]


def test_hello():
    deck = FrenchDeck()
    assert deck[0].suit == "spades"
    assert len(deck) == (13 * 4)


suit_values = dict(spades=0, diamonds=1, clubs=2, hearts=3)


def sort_fun(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def test_sort():
    deck = FrenchDeck()
    ndeck = sorted(deck, key=sort_fun)
    print(ndeck)
