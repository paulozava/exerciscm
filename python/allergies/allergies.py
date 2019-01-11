class Allergies(object):

    def __init__(self, score):
        self.__allergies_table = {1: 'eggs', 2: 'peanuts', 4: 'shellfish', 8: 'strawberries',
                                  16: 'tomatoes', 32:'chocolate', 64: 'pollen', 128: 'cats'}
        self.__score = score
        self.__allergies = self.__found_allergies()

    def is_allergic_to(self, item):
        return item.lower() in self.__allergies

    def __found_allergies(self):
        counter = self.__score
        allergies = []
        divisions = 7 + (counter//128)
        for i in range(divisions, -1, -1):
            i = 2 ** i
            if counter // i == 1:
                if i <= 128:
                    allergies.append(self.__allergies_table[i])
                counter -= i
        return allergies


    @property
    def lst(self):
        return self.__allergies