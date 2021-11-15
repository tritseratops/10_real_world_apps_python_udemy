from datetime import datetime
def day_today(date_str):
    my_date = datetime.strptime(date_str, '%Y-%m-%d')
    return my_date.strftime('%A')

print(day_today("2019-6-17"))