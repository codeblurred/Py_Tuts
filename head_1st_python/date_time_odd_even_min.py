'''
This is from  headfirst python book .
Also check the github about the commits to know more

'''

from datetime import datetime, date
import random
import time


odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

time_now = datetime.now()
print("Time now :", time_now)

today = date.today()
print("today's date :", today)

for i in range (5):
    right_this_min = datetime.today().minute
    #### this is a variable wherein we are storing the value as generated out of  datetime.today().minute

    if right_this_min in odds:
        print("this minute seems a little odd")
    else:
        print("not an odd minute")
    wait_time = random.randint(1,60)
    print(" The random generated seconds : ",wait_time)
    time.sleep(wait_time)
