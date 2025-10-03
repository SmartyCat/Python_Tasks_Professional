from datetime import datetime, timedelta, date

t = datetime.strptime(input(), "%H:%M:%S")
print((t + timedelta(seconds=int(input()))).time())
