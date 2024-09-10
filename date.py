#witre a program to chect excet date ande time.
import datetime
now=datetime.datetime.now()
print("current date and time is:")
print(now.strftime("%y-%m-%d %H:%M:%S"))