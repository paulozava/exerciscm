from __future__ import division
from functools import reduce


class Rational(object):
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError
        self.numerator = numerator
        self.denominator = denominator
        self.signal = reduce(lambda x,y: x*y,
                             [1 if numerator >= 0 else -1, 1 if denominator >= 0 else -1])

    def __eq__(self, other):
        numerator_min, numerator_max = tuple(sorted([abs(self.numerator), abs(other.numerator)]))
        denominator_min, denominator_max = tuple(sorted([abs(self.denominator), abs(other.denominator)]))
        if (numerator_min, numerator_max) == (0, 0):
            return True
        else:
            return numerator_max % numerator_min == 0 \
                   and denominator_max % denominator_min == 0 \
                   and self.signal == other.signal

    def __repr__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        numerator = (self.numerator * other.denominator + other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = (self.numerator * other.denominator - other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = other.numerator * self.denominator
        if denominator != 0:
            return Rational(numerator, denominator)
        raise ZeroDivisionError

    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power):
        ratio = [self.numerator ** abs(power), self.denominator ** abs(power)]
        if power < 0:
            ratio.reverse()
        return Rational(*ratio)

    def __rpow__(self, base):
        return base ** (self.numerator/self.denominator)
