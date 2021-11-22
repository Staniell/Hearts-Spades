"""
Author:
Collaboration Acknowledgement: Cite any help that you may have got here.
"""
import random
POKER_HANDS = ['Royal flush', 'Straight flush', 'Four of a kind', 'Full house',\
               'Flush', 'Straight', 'Three of a kind', 'Two pair', 'One pair',\
               'High Card']
SUITS = 'HSDC'
KINDS = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
STRAIGHTS = [KINDS[i:(i+5)] for i in range(9)] + [['A','5','4','3','2']]
NUM_HANDS = 10000

def deal_hand():
    # Returns a randomly dealt 5-card hand
    initial = list(range(52))
    for i in range(5):
        j = random.randint(i, 51)
        initial[i], initial[j] = initial[j], initial[i]
    result = []
    for card in initial[:5]:
        suit = SUITS[card//13]
        kind = KINDS[card%13]
        result.append( suit+kind )
    return result
        
##### DO NOT MODIFY ABOVE THIS LINE; NEED TO FIX CODE BELOW (WITH DOCSTRINGS)!!!

def sort_hand( hand ):
    """

    >>> sort_hand(['H9', 'CJ', 'S9', 'S7', 'DJ'])
    ['DJ', 'CJ', 'H9', 'S9', 'S7']
    >>> sort_hand(['C4', 'D2', 'DA', 'C3', 'S5'])
    ['DA', 'S5', 'C4', 'C3', 'D2']
    """
    cards = hand
    KINDS = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    SUITS = ["H","S","C","D"]
    final_hand = sorted(cards, key=lambda x: (KINDS.index(x[1]),SUITS.index(x[0])))



    return final_hand


def label_hand( hand ):
    """

    >>> label_hand(['D8', 'D10', 'D7', 'DJ', 'D9'])
    ('Flush', ['DJ', 'D10', 'D9', 'D8', 'D7'])
    >>> label_hand(['C4', 'D2', 'DA', 'C3', 'S5'])
    ('Straight', ['DA', 'S5', 'C4', 'C3', 'D2'])
    """
    hand = sort_hand(hand)
    outcome = ''
    kinds = ['A', 'K', 'Q', 'J','10', '9', '8', '7', '6', '5', '4', '3', '2']
    kinds_sequence = {"A": 14, "K": 13, "Q": 12, "J": 11}
    suits = ['H', 'S', 'D', 'C']

    straight_flush = ['5', '4', '3', '2', 'A']

    kinds_cards = []
    suits_cards = {}

    flushCheck = {1: {0: "Flush", 4: "Straight Flush", 5:"Royal Flush"}, 2:{4:"Straight"}}
    patternCheck = {4:"Four of a kind",3:"Three of a kind",2:"Full house", 1:"Two Pair", 0:"One Pair", 5:"High Pair"}

    for i in hand:
        if i[0] not in suits_cards:
            suits_cards[i[0]] = 1
        else:
            suits_cards[i[0]] += 1
        kinds_cards.append(i[1:])


    sequence = 0

    for i in range(len(hand) - 1):
        if hand[i+1][1] == '2':
            if hand[-1][1] == '2' and hand[0][1] == "A":
                sequence+=1
        if hand[i][1] in kinds_sequence and hand[i + 1][1] in kinds_sequence:
            checker = kinds_sequence[hand[i][1]] - kinds_sequence[hand[i + 1][1]]
            if checker == 1:
                sequence += 1
        elif hand[i][1] in kinds_sequence and hand[i + 1][1:] not in kinds_sequence:
            checker = kinds_sequence[hand[i][1]] - int(hand[i + 1][1:])
            if checker == 1:
                sequence += 1
        elif hand[i][1] not in kinds_sequence and hand[i+1][1:] in kinds_sequence:
            checker = int(hand[1][1:]) - kinds_sequence[hand[i+1][1]]
            if hand[i][1] == '2' and hand[i+1][1] == "A":
                sequence += 1
        else:
            checker = int(hand[i][1:]) - int(hand[i + 1][1:])
            if checker == 1:
                sequence += 1

    counter = []
    result = 0


    for i in kinds:
        counter.append(kinds_cards.count(i))


    if counter.count(2) > counter.count(1): #Two pair
        result = 1
    else: #One pair
        result = 0

    if 4 in counter: #Four of a kind
        result = 4
    if 3 in counter: #Three of a kind
        result = 3
        if 3 and 2 in counter: #Full House
            result = 2

    if len(suits_cards) > 3 and counter.count(1) == 5:
        result = 5

    if sequence != 4:
        sequence = 0
    elif sequence == 4 and set(kinds_cards).issubset(kinds[0:5]):
        sequence = 5
    elif sequence == 4 and set(kinds_cards).issubset(straight_flush):
        sequence = 4

    if len(suits_cards) == 1:
        x = flushCheck[len(suits_cards)]
        outcome = x[sequence]

    elif len(suits_cards) > 1:
        if sequence == 4:
            x = flushCheck[2]
            outcome = x[sequence]
        else:
            outcome = patternCheck[result]


    return (outcome, hand)


def frq_patterns():
    """

    """
    patternCount = {'Full house': 0, 'Three of a kind': 0, 'Two pair': 0}

    def random_suits(n=5):
        return [
            random.choice(SUITS)
            for _ in range(n)
        ]

    def make_hand(suits, ranks):
        return [
            suit + rank
            for suit, rank in zip(suits, ranks)
        ]

    sample = [
        make_hand(random_suits(), random.choice(STRAIGHTS))
        for _ in range(1000)
    ]
    for i in sample:
        print(label_hand(i))


    return {'Full house': 0, 'Three of a kind': 0, 'Two pair': 0}

### ADD MORE OF YOUR OWN DOCTESTS TO THE FIRST TWO FUNCTION DOCSTRINGS!!!
### DO NOT MODIFY THE MAIN BLOCsK BELOW!!!

if __name__ == "__main__":
    import doctest
    doctest.testmod()
