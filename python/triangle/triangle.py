def is_triangle(sides):
    a, b, c = tuple(sides)
    return a > 0 and b > 0 and c > 0 and a + b >= c and a + c >= b and b + c >=a

def is_equilateral(sides):
    if is_triangle(sides):
        a, b, c = tuple(sides)
        return a == b == c
    else:
        return False


def is_isosceles(sides):
    if is_triangle(sides):
        a, b, c = tuple(sides)
        return a == b or a == c or b == c
    else:
        return False

def is_scalene(sides):
    if is_triangle(sides):
        a, b, c = tuple(sides)
        return a != b != c
    else:
        return False
