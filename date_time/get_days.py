from datetime import date, timedelta
import calendar


def get_days_in_month(y, m):
    inde = list(calendar.month_name).index(m)
    d = calendar.monthrange(y, inde)[1]

    return [date(y, inde, 1) + timedelta(days=i) for i in range(d)]


print(get_days_in_month(2021, "March"))
