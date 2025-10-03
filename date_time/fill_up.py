from datetime import datetime, timedelta


def fill_up_missing_dates(dates):
    dates = sorted(map(lambda x: datetime.strptime(x, "%d.%m.%Y").date(), dates))
    result = [dates[0]]
    for index, item in enumerate(dates[1:]):
        if (item - dates[index + 1]).days != 1:
            while (result[-1] - dates[index + 1]).days != 1:
                result.append(result[-1] + timedelta(days=1))
        else:
            result.append(item)
    return [i.strftime("%d.%m.%Y") for i in result[:-1]]


dates = ["01.11.2021", "07.11.2021", "04.11.2021", "03.11.2021"]
print(fill_up_missing_dates(dates))

dates = ["01.11.2021", "04.11.2021", "09.11.2021", "15.11.2021"]
print(fill_up_missing_dates(dates))
