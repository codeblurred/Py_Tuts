from datetime import datetime
from datetime import date

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]


for i in range (5):
# Loop a specified no.s of time

    right_this_min = datetime.today().minute

    if right_this_min in odds:
        print("this min seems a little odd")
    else:
        print("not an odd min ")
