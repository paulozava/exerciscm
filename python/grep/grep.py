def grep(pattern, files='/home/laumzav/PycharmProjects/exerciscm/python/grep/test', flags=''):
    '''
    :param pattern:
    :param files:
    :param flags:
        -n Print the line numbers of each matching line.
        -l Print only the names of files that contain at least one matching line.
        -i Match line using a case-insensitive comparison.
        -v Invert the program -- collect all lines that fail to match the pattern.
        -x Only match entire lines, instead of lines that contain a match.
    :return:
    '''

    with open(files) as f:
        targets = f.readlines()

    if 'l' in flags and any(map(lambda x: pattern in x, targets)):
        print(files)
        return 0

    if 'i' in flags:
        pattern = pattern.lower()

    for row, target in enumerate(targets):
        if 'i' in flags:
            target = target.lower()

        if 'v' in flags:
            invert_search(flags, pattern, row, target, targets)
        elif 'x' in flags:
            full_search(flags, pattern, row, target, targets)
        else:
            basic_search(flags, pattern, row, target, targets)
    return 0


def basic_search(flags, pattern, row, target, targets):
    if pattern in target:
        flag_n(flags, row)
        print(targets[row].replace('\n', ''))

def invert_search(flags, pattern, row, target, targets):
    if pattern not in target:
        flag_n(flags, row)
        print(targets[row].replace('\n', ''))

def full_search(flags, pattern, row, target, targets):
    if pattern + '\n' in target:
        flag_n(flags, row)
        print(targets[row].replace('\n', ''))

def flag_n(flags, row):
    if 'n' in flags:
        print(row + 1, end=':')
