class Clock(object):
    def __init__(self, hour, minute):
        self.accumulated = 0
        self.__acc__(hour, minute)
        self.__circulate__()

    def __repr__(self):
        time = divmod(self.accumulated, 60)
        return '{:0>2}:{:0>2}'.format(*time)

    def __eq__(self, other):
        return self.accumulated == other.accumulated

    def __add__(self, minutes):
        self.accumulated += minutes
        self.__circulate__()
        return self.__repr__()

    def __sub__(self, minutes):
        self.accumulated -= minutes
        self.__circulate__()
        return self.__repr__()

    def __acc__(self, hour, minute):
        acc = (hour%24) * 60 if hour >= 0 else (24 - abs(hour)%24) * 60
        acc += minute
        self.accumulated = acc

    def __circulate__(self):
        self.accumulated %= 1440