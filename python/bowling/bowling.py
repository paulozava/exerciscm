class BowlingGame(object):
    def __init__(self):
        self.points = 0
        self.pins = []
        self.plays = []

    def roll(self, pin):
        if pin == 10:
            self.pins.extend([pin, 0])
        else:
            self.pins.append(pin)

    def score(self):
        length = len(self.pins) if len(self.pins) <= 20 else 20
        for index in range(0, length, 2):
            if self.pins[index] == 10:
                pin_value = sum(self.pins[index:index+4])
            elif sum(self.pins[index:index+2]) == 10:
                partial = sum(self.pins[index:index + 3])
                pin_value = 20 if partial>20 else partial
            else:
                pin_value = sum(self.pins[index:index + 2])
            self.plays.append(pin_value)
        self.points = sum(self.plays)
        return self.points