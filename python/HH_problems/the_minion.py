# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    winner = {'Kevin': 0, 'Stuart': 0}
    string_len = len(string)
    for i in range(string_len):
        if string[i] in 'AEIOU':
            winner['Kevin'] += string_len - i
        else:
            winner['Stuart'] += string_len - i
    if winner['Kevin'] > winner['Stuart']:
        print('Kevin ' + str(winner["Kevin"]))
    elif winner['Kevin'] < winner['Stuart']:
        print('Stuart ' + str(winner["Stuart"]))
    else:
        print('Draw')


    t = int(len(string) / k)
    for i in range(t, len(string)+1, t):
        mu = ''
        for candidate in string[i-t:i]:
            if candidate not in mu:
                mu += candidate
        print(mu)
