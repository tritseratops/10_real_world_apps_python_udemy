import datetime, time

backghround_same_start_time = datetime.datetime.now()
time.sleep(5)
sec_from_motion_start = (datetime.datetime.now()-backghround_same_start_time).total_seconds()
print(sec_from_motion_start)