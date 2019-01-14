def append(xs, ys):
    xs.extend(ys)
    return xs


def concat(lists):
    resp = []
    for item in lists:
        resp.extend(item)
    return resp


def filter_clone(function, xs):
    return [item for item in xs if function(item)]


def length(xs):
    count = 0
    while xs:
        _ = xs.pop()
        count += 1
    return count


def map_clone(function, xs):
    return [function(item) for item in xs]


def foldl(function, xs, acc):
    for item in xs:
        acc = function(item, acc)
    return acc



def foldr(function, xs, acc):
    for item in reverse(xs):
        acc = function(item, acc)
    return acc



def reverse(xs):
    sx = []
    if xs:
        while xs:
            item = xs.pop()
            sx.append(item)
    return sx
