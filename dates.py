import datetime

def dates():
    today = datetime.datetime.today()
    year = today.year

    new_year = datetime.date(year, 1, 1)
    new_year_day = new_year.weekday()
    difference = datetime.timedelta(6 - new_year_day)
    first_sunday = new_year + difference
    dates = [list() for x in range(7)]

    for x in range(7*51):
        dates[x % 7].append(first_sunday + datetime.timedelta(x))
    return dates
