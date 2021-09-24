import datetime
import calendar
import math
from queue import Queue
from collections import deque

def gen_pairs(datelist):
    tuplelist = []
    dq = deque(datelist)
    while(len(dq) > 1):
        start = dq.popleft()
        end = dq[0]
        tuplelist.append(
                (start,end)
                )
    return tuplelist

def gen_dates():
    start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
    end = datetime.datetime.strptime("01-01-2020", "%d-%m-%Y")
    nmonths = math.ceil((end-start).days/31)+1
    print(nmonths)
    datelist = [(start + datetime.timedelta(days=x*31)).strftime('%Y%m%d') for x in range(0, nmonths)]

    return gen_pairs(datelist)

def get_time_range_list(startdate, enddate):
    """
    Get a list of time parameters
         : param startdate: start month start time-> str 
         : param enddate: end time-> str
    :return: date_range_list -->list
    """
    date_range_list = []
    while 1:
        next_month = startdate + datetime.timedelta(days=calendar.monthrange(startdate.year, startdate.month)[1])
        month_end = next_month - datetime.timedelta(days=1)
        if month_end < enddate:
            date_range_list.append((datetime.datetime.strftime(startdate,
                                                               '%Y%m%d'),
                                    datetime.datetime.strftime(month_end,
                                                               '%Y%m%d')))
            startdate = next_month
        else:
            return date_range_list

    return 'error'
