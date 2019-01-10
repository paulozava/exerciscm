def decode(string):
    response, digit_acc = '', ''
    for character in string:
        if character.isdigit():
            digit_acc += character
        else:
            multiplier = int(digit_acc) if digit_acc.isdigit() else 1
            response += multiplier * character
            digit_acc = ''
    return response


def encode(string):
    try:
        previous, counter, response = string[0], 1, ''
        string+='¢'
        for letter in string[1:]:
            if letter != previous:
                response += f'{counter if counter > 1 else ""}{previous}'
                counter = 1
                previous = letter
            else:
                counter +=1
        return response
    except:
        return string