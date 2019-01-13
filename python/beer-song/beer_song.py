def recite(start=2, take=1):
    poetry = []
    pluralize = lambda x: "s" if x > 1 else ""
    for bottle in range(start, start-take, -1):
        if poetry:
            poetry.append('')
        if bottle > 1:
            poetry.append(f'{bottle} bottle{pluralize(bottle)} of beer on the wall,'
                       f' {bottle} bottle{pluralize(bottle)} of beer.')
            poetry.append(f'Take one down and pass it around, {bottle - 1} '
                       f'bottle{pluralize(bottle-1)} of beer on the wall.')
        elif bottle == 1:
            poetry.extend(["1 bottle of beer on the wall, 1 bottle of beer.",
                        "Take it down and pass it around, no more bottles of beer on the wall."])
        elif bottle == 0:
            poetry.extend(["No more bottles of beer on the wall, no more bottles of beer.",
                        "Go to the store and buy some more, 99 bottles of beer on the wall."])
    return poetry