def flatten(iterable):
    while True in [isinstance(it, (list, tuple)) for it in iterable]:
        partial = list()
        for iter in iterable:
            if isinstance(iter, (list, tuple)):
                partial.extend(iter)
            else:
                partial.append(iter)
        iterable = list(partial)
    while None in iterable:
        iterable.remove(None)
    return iterable