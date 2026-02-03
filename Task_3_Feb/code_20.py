'''20. Date Range Generator
Input: start = 2025-07-01, end = 2025-07-04
Output: ['2025-07-01', '2025-07-02', '2025-07-03', '2025-07-04']'''
from datetime import datetime, timedelta

start_day = "2025-07-01"
end_day = "2025-07-04"

start_date = datetime.strptime(start_day, "%Y-%m-%d")
end_date = datetime.strptime(end_day, "%Y-%m-%d")

date_list = []

while start_date <= end_date:
    date_list.append(start_date.strftime("%Y-%m-%d"))
    start_date += timedelta(days=1)

print(date_list)