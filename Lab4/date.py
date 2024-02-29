import datetime

# ex 1

today= datetime.datetime.now()

minus_five = today - datetime.timedelta(days = 5)

print(minus_five.strftime("%y-%m-%d"))
print(today.strftime("%Y-%m-%d"))

# ex 2 

today= datetime.datetime.now()

yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)


print(yesterday.strftime("%y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

# ex 3 

Now = datetime.datetime.now()

without = Now.replace(microsecond=0)

print(without)

# ex 4

from datetime import datetime

current_data = datetime.now()
my_data = datetime(2024, 8, 11, 15, 1, 0)

difference_sec = (current_data - my_data).total_seconds()

print(difference_sec)