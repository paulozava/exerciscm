class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self):
        if not self.card_num.startswith(' '):
            card = self.card_num.replace(' ', '')
            if card.isdigit():
                doubling = lambda x: int(x) * 2 if int(x) * 2 <= 9 else (int(x) * 2) - 9
                verify_digit = sum([doubling(number) if position % 2 != 0
                                    else int(number)
                                    for position, number in enumerate(card)])
                return verify_digit % 10 == 0
        return False