from operator import add, truediv, sub, mul
import re

class StackUnderflowError(Exception):
    def __init__(self, message='Stack Underflow Error'):
        super().__init__(message)

def evaluate(input_data):
    data = ''.join(input_data)

    data = do_arithmetic_calc(data)
    data = do_stack_mods(data)

    try:
        return [int(i) for i in data.split()]
    except:
        raise StackUnderflowError()


def do_arithmetic_calc(data):
    pattern = '[0-9]+ [0-9]+ [+\-*/]'
    while re.match(pattern, data):
        for item in re.findall(pattern, data):
            result = eval('{0}{2}{1}'.format(*item.split()))
            if '/' in item:
                result = int(result)
            data = data.replace(item, str(result))
    return data

def do_stack_mods(data):
    dup = r'\d+ dup'
    for item in re.findall(dup, data):
        i, op = tuple(item.split())
        data = data.replace(item, f'{i} {i}')

    drop = r'\d+ drop'
    for item in re.findall(drop, data):
        data = str.strip(data.replace(item, ''))

    swap = r'\d+ \d+ swap'
    for item in re.findall(swap, data):
        a, b, op = tuple(item.split())
        data = data.replace(item, '{} {}'.format(b, a))

    over = r'\d+ \d+ over'
    for item in re.findall(over, data):
        a, b, op = tuple(item.split())
        data = data.replace(item, '{} {} {}'.format(a, b, a))

    return data