##unfinished

def transpose(input_lines=None):
    lines = input_lines.split()
    max_inline = max(map(len, lines))
    if len(lines) <= 1:
        return '\n'.join(list(input_lines))
    elif max_inline == 1:
        return ''.join(lines)
    else:
        squared_lines = [line + ' ' * (max_inline - len(line)) for line in lines]
        transposed_lines = [''.join(element) for element in zip(*squared_lines)]
        return '\n'.join(transposed_lines)
