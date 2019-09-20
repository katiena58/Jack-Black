class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def word_to_number(self):
        if self.rank == "two":
            return "2"
        elif self.rank == "three":
            return "3"
        elif self.rank == "Four":
            return "4"
        elif self.rank == "Five":
            return "5"
        elif self.rank == "Six":
            return "6"
        elif self.rank == "Seven":
            return "7"
        elif self.rank == "Eight":
            return "8"
        elif self.rank == "Nine":
            return "9"
        elif self.rank == "Ten":
            return "10"
        elif self.rank == "Jack":
            return "J"
        elif self.rank == "Queen":
            return "Q"
        elif self.rank == "King":
            return "K"
        elif self.rank == "Ace":
            return "A"

    def __str__(self):
        return (
            '┌─────────┐\n'
            ' │{}       │\n'
            ' │         │\n'
            ' │         │\n'
            ' │    {}   │\n'
            ' │         │\n'
            ' │         │\n'
            ' │       {}│\n'
            ' └─────────┘\n'
        ).format(
            format(self.word_to_number(), ' <2'),
            format(self.suit, ' <2'),
            format(self.word_to_number(), ' >2')
        )
