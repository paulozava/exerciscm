from functools import reduce

def slices(series, length):
    if len(series) < 0 or length < 1 or length > len(series):
        raise ValueError('Invalid parameters')
    start, end = 0, length
    return [series[start+crawler:end+crawler]
            for crawler in range(len(series)-length+1)]

def largest_product(series, size):
    return max([reduce(lambda x, y: int(x) * int(y), i)
                for i in map(list, slices(series, size))])