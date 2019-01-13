## clever soulution that i found to this problem ;D

def is_paired(string):
    pairs = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in string:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if not stack or char != pairs[stack.pop()]:
                return False

    return not stack