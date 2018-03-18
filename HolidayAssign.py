from datetime import date


class HolidayAssign:
    def __init__(self):
        self._create_dict = {}

    @staticmethod
    def file_len(f_name):
        with open(f_name) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    @staticmethod
    def create_dict():
        count = 0
        # open the files
        march_holidays = open("marchholidays.txt", "r")
        march_dates = open("marchdates.txt", "r")

        current_date = march_dates.readline(count)
        current_holiday = march_holidays.readline(count)

        num_dates = HolidayAssign.file_len("marchdates.txt")
        # initialize an empty dictionary
        holidays = {}

        # loop through the dates in the dates file
        while count < num_dates:
            holidays[march_dates.readline(count)] = march_holidays.readline(count)
            # at each date key, place
            # holidays[count] = march_dates.readline(count)
            count += 1

        # count2 = 0
        # for holiday in march_holidays:
        #     holidays[holidays[count2]] = march_holidays.readline(count2)
        #     count2 += 1

        # Debugging by printing dictionary contents
        for d in holidays:
            print(d)
            print(holidays[d])
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
