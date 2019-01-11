# Score categories
# Change the values as you see fit

CHOICE = lambda x: sum(x)
ONES = lambda x: x.count(1) * 1
TWOS = lambda x: x.count(2) * 2
THREES = lambda x: x.count(3) * 3
FOURS = lambda x: x.count(4) * 4
FIVES = lambda x: x.count(5) * 5
SIXES = lambda x: x.count(6) * 6
LITTLE_STRAIGHT = lambda x: 30 if sorted(x) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda x: 30 if sorted(x) == [2,3,4,5,6] else 0
FULL_HOUSE = lambda x: sum(x) if x.count(max(x, key=x.count)) == 3 and len(set(x)) == 2 else 0
FOUR_OF_A_KIND = lambda x: max(x, key=x.count) * 4 if x.count(max(x, key=x.count)) >= 4 else 0
YACHT = lambda x: 50 if len(set(x)) == 1 else 0

def score(dice, category):
    return category(dice)
