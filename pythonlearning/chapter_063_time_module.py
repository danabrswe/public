# epoch =   (also pronounced "epic") a date an time from which a computer measures system time

import time

print(time.ctime(0))                # converts time expressed in seconds to readable string
print(time.ctime(1000000))          # outputs datetime one million seconds after epoch
print(time.time())                  # return current time according to your system, in seconds since epoch
print(time.ctime(time.time()))      # converts current time to readable string
print("---")

time_object = time.localtime()      # creates a time object
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S CET", time_object)        # converts time object to string using given string format
gm_time = time.strftime("%B %d %Y %H:%M:%S GMT", time.gmtime())         # same but in GMT
print(local_time)
print(gm_time)
print("---")

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)
print(time.strftime("%B %d %Y %H:%M:%S CET", time_object))
print("---")

# (year, month, day, hours, minutes, secs, day_of_the_week, day_of_the_year, daylight_savings_time)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, -1)
print(time.asctime(time_tuple))
print("---")

# convert to seconds since epoch
print(time.mktime(time_tuple))
print(time.mktime(time_object))