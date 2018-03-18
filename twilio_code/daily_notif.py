import time, calendar
from datetime import datetime
from twilio_code.HolidayAssign import HolidayAssign


def daily():
    # Dictionary of Dates to Holidays
    holidayList = HolidayAssign()
    date_holiday_dict = holidayList.create_dict()

    monthdict = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May",
                 "06": "June", "07": "July", "08": "August", "09": "September", "10": "October",
                 "11": "November", "12": "December"}

    for holiday in date_holiday_dict.keys():
        holidays = date_holiday_dict.keys()

        holiday_month = holiday[0: holiday.find(" ")]
        holiday_date = holiday[holiday.find(" ") + 1:len(holiday)]

        to_day = datetime.now()

        today_month = monthdict[to_day.strftime("%m")]

        if holiday_month == today_month and holiday_date == to_day.strftime("%d"):
            print("Today is: " + date_holiday_dict[holiday])
            # time.sleep(10)

if __name__ == "__main__":
    daily()
