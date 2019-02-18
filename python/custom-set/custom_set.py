class CustomSet(object):
    def __init__(self, elements=None):
        self.elements = list()
        if elements:
            self.__add__(elements)

    def __contains__(self, element):
        return True if element in self.elements else False

    def __eq__(self, other):
        e_self = sorted(self.elements)
        o_self = sorted(other.elements)
        return e_self == o_self

    def __sub__(self, elements):
        if isinstance(elements, CustomSet):
            elements = elements.elements
        try:
            for element in elements:
                if element in self.elements:
                    self.elements.remove(element)
            return self
        except:
            raise TypeError('CustomSet - object is not iterable')

    def __add__(self, elements):
        if isinstance(elements, CustomSet):
            elements = elements.elements
        try:
            for element in elements:
                if element not in self.elements:
                    self.elements.append(element)
            return self
        except:
            raise TypeError('CustomSet - object is not iterable')


    def __str__(self):
        return '<{}>'.format(str(self.elements))

    def add(self, element):
        if isinstance(element, (int, float, str)):
            element = [element]
        self.__add__(element)

    def intersection(self, other):
        inter = [element
                for element in self.elements
                if element in other.elements]
        return CustomSet(inter)

    def isempty(self):
        return False if self.elements else True

    def issubset(self, other):
        return all([True if element in other.elements else False
                    for element in self.elements])

    def isdisjoint(self, other):
        return all([True if element not in other.elements else False
                    for element in self.elements])
