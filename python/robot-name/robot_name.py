from secrets import choice, randbelow
from string import ascii_uppercase as letters

class Robot(object):
    def __init__(self):
        self.name = self.rand_name()

    def rand_name(self):
        first = "".join([choice(letters) for _ in range(2)])
        second = randbelow(1000)
        return '{}{:03}'.format(first, second)

    def reset(self):
        self.name = self.rand_name()