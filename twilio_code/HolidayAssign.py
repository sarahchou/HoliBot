import collections


class HolidayAssign:
    def __init__(self):
        self._create_dict = {}

    @staticmethod
    def create_dict():
        # open the files
        all_holidays = open("allholidays.txt", "r")

        # initialize an empty dictionary
        holidays = collections.OrderedDict()

        # loop through the dates in the dates file
        with open('alldates.txt') as f:
            for line in f:
                holidays[line.rstrip()] = all_holidays.readline()

        return holidays

    def output(self, body):
        num = 0
        dictionary = self.create_dict()
        for i in dictionary:
            if body == dictionary[num]:
                out = dictionary[body]
        return out


if __name__ == "__main__":
    HolidayAssign.create_dict()
