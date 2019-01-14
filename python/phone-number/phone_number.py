class Phone(object):
    def __init__(self, phone_number):
        self._raw_number = phone_number
        self._cleaned_number = self._parse_number()
        self.area_code = self._cleaned_number[:3]
        self.max_region = self._cleaned_number[3:6]
        self.min_region = self._cleaned_number[6:]

    def _parse_number(self):
        number = self._raw_number
        clean_number = ''.join([digit for digit in number if digit not in '()- .+'])
        if not clean_number.isdigit():
            raise ValueError('Invalid digits')
        if not self._is_valid_number(clean_number):
            raise ValueError('It is not a valid number')
        return clean_number[1:] if len(clean_number) == 11 else clean_number

    def _is_valid_number(self, number):
        is_valid_area_exc = lambda x, y: x not in '01' and y not in '01'

        if len(number) == 11 and number[0] == '1':
            number = number[1:]
        return len(number) == 10 and is_valid_area_exc(number[0], number[3])

    def number(self):
        return self._cleaned_number

    def pretty(self):
        return f'({self.area_code}) {self.max_region}-{self.min_region}'