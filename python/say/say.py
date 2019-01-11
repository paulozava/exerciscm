###### unfinished

def say(number):
    if number < 0 or number >= 1e12:
        raise ValueError('Out of bound')
    elif number < 100:
        dezene = (number // 10) * 10
        unit = number - dezene
        if unit == 0:
            return f'{number_to_extensive[dezene]}'
        else:
            return f'{number_to_extensive[dezene]}-{number_to_extensive[unit]}'
    elif number < 1000:
        centene = (number // 100)
        dezene = number - centene


def dezenes(number):
    number_to_extensive = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13: 'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',80:'eighty', 90:'ninety'}
    if 0 <= number < 20:
        return number_to_extensive[number]
    dezene = (number // 10) * 10
    unit = number - dezene
    if unit == 0:
        return f'{number_to_extensive[dezene]}'
    else:
        return f'{number_to_extensive[dezene]}-{number_to_extensive[unit]}'