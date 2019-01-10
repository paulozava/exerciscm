from datetime import date, timedelta

DOTW = {'Monday': 0, 'Tuesday': 1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
WHICH_POSITIONS = {'1st':0, '2nd':1, '3rd':2, '4th':3, '5th':4, 'last':-1}

def meetup_day(year, month, day_of_the_week, which):
    days_of_month = date(year=year, month=month, day=1)
    dotw_seek = DOTW[day_of_the_week]
    days_in_dotw = []
    while days_of_month.month == month:
        if dotw_seek == days_of_month.weekday():
            days_in_dotw.append(days_of_month)
        days_of_month += timedelta(days=1)
    date_response = days_in_dotw[WHICH_POSITIONS[which]]
    return date_response