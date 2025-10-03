from datetime import time, timedelta

s = time.fromisoformat(input())
print(s.hour * 3600 + s.minute * 60 + s.second)
