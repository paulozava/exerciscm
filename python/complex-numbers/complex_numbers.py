from math import exp, cos, sin

class ComplexNumber(object):
    '''
    The sum/difference of two complex numbers involves adding/subtracting their real and imaginary parts separately: (a + i * b) + (c + i * d) = (a + c) + (b + d) * i, (a + i * b) - (c + i * d) = (a - c) + (b - d) * i.

Multiplication result is by definition (a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i.

The reciprocal of a non-zero complex number is 1 / (a + i * b) = a/(a^2 + b^2) - b/(a^2 + b^2) * i.

Dividing a complex number a + i * b by another c + i * d gives: (a + i * b) / (c + i * d) = (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i.

Exponent of a complex number can be expressed as exp(a + i * b) = exp(a) * exp(i * b), and the last term is given by Euler's formula exp(i * b) = cos(b) + i * sin(b).
    '''
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __mul__(self, other):
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __truediv__(self, other):
        # (a * c + b * d) / (c ^ 2 + d ^ 2) + (b * c - a * d) / (c ^ 2 + d ^ 2) * i.
        new_real = (self.real * other.real + self.imaginary * other.imaginary)/(other.real**2 + other.imaginary**2)
        new_imaginary = (self.imaginary * other.real - self.real * other.imaginary)/(other.real^2 + other.imaginary**2)
        return ComplexNumber(new_real, new_imaginary)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2)**(1/2)

    def conjugate(self):
        real, imaginary = self.real, -1 * self.imaginary
        return ComplexNumber(real, imaginary)

    def exp(self):
        real = exp(self.real) * cos(self.imaginary)
        imaginary = exp(self.real) * sin(self.imaginary)
        return ComplexNumber(real, imaginary)