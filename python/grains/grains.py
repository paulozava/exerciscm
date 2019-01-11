def on_square(square_number):
    if not (0 < square_number < 65):
        raise ValueError('Value impossible')
    return 2 ** (square_number - 1)


def total_after(square_number):
    if not (0 < square_number < 65):
        raise ValueError('Value impossible')
    square_acc, square_grain = 0, 1
    for _ in range(square_number):
        square_grain *= 2
        square_acc += square_grain
    return square_grain
