def raindrops(number):
    response = ''
    if number % 3 == 0: response += 'Pling'
    if number % 5 == 0: response += 'Plang'
    if number % 7 == 0: response += 'Plong'
    if response is '': response = str(number)
    return response