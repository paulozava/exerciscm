def numeral(number):
    if number > 3999: return False
    romans_dezenes = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX', 40:'XL', 50:'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'}

    numbers = str(number)
    zero_format = len(numbers)
    numbers_decomposion = []
    for i in numbers:
        i_formatted = i + (zero_format - 1) *'0'
        numbers_decomposion.append(int(i_formatted))
        zero_format-=1

    numbers_romanized = [romans_dezenes[i] for i in numbers_decomposion]
    response = ''.join(numbers_romanized)
    return response