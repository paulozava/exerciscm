SHAKES = ['wink', 'double blink', 'close your eyes', 'jump']

def handshake(code):
    bincode, reverse_it = bin(code)[2:], False
    bincode_len = len(bincode)
    if bincode_len > 5:
        raise ValueError("You're not supposed to be here!")
    elif bincode_len == 5:
        bincode = bincode[:0:-1]
        reverse_it = True
    else:
        bincode = '0' * (4 - bincode_len) + bincode
        bincode = bincode[::-1]
    handshakes = [shake for code, shake in zip(bincode, SHAKES) if code == '1']
    if reverse_it:
        handshakes.reverse()
    return handshakes

def secret_code(actions):
    checked = ''.join(['1' if shake in actions else '0' for shake in reversed(SHAKES)])
    if SHAKES.index(actions[0]) > SHAKES.index(actions[-1]):
        checked = '1' + checked
    return int(checked, 2)
