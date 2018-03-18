import collections


class HolidayAssign:
    def __init__(self):
        self._create_dict = {}

    @staticmethod
    def create_dict():
        # open the files
        march_holidays = open("marchholidays.txt", "r")

        # initialize an empty dictionary
        holidays = collections.OrderedDict()

        # loop through the dates in the dates file
        with open('marchdates.txt') as f:
            for line in f:
                holidays[line.rstrip()] = march_holidays.readline()

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
