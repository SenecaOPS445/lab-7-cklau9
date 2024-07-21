#!/usr/bin/env python3
# Student ID: cklau9
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    # """Add two time objests and return the sum."""
    # sum = Time(0,0,0)
    # sum.hour = t1.hour + t2.hour
    # sum.minute = t1.minute + t2.minute
    # sum.second = t1.second + t2.second
    # #[ insert python code here to check for minute and second 
    # #[ attribute here, and carry over when necessary
    # #[
    # if sum.second >= 60: # Check the sum.second greater than 60 seconds
    #     sum.second = sum.second - 60 # Adjust sum.second shall minus 60
    #     sum.minute = sum.minute + 1 # Adjust sum.minute by add 1
    # if sum.minute >= 60: # Check the sum.minute greater than 60 minutes
    #     sum.minute = sum.minute - 60 # Adjust sum.minute shall minus 60
    #     sum.hour = sum.hour + 1 # Adjust sum.hour by add 1
    # return sum
    t1_to_sec = time_to_sec(t1)
    t2_to_sec = time_to_sec(t2)
    sum_of_sec = t1_to_sec + t2_to_sec
    return sec_to_time(sum_of_sec)

def change_time(time, seconds):
    # time.second += seconds
    # #if valid_time(time) != True:
    
    # # calculate the time if seconds and/or minute >= 60 
    # while time.second >= 60:
    #     time.second -= 60
    #     time.minute +=1
    # while time.minute >= 60:
    #     time.minute -= 60
    #     time.hour += 1
    
    # # calculate the time if seconds and/or minute <= 0 
    # while time.second < 0: # Do while loop to handle negative second input 
    #     time.minute -= 1 # Deduct 1 minute, then add 60 seconds
    #     time.second += 60 # New second add 60 seconds
    # while time.minute < 0: # Do while loop while negative minute generated
    #     time.hour -= 1 # Deduct 1 hr, then add 60 minutes
    #     time.minute += 60
    total_sec_change_time = time_to_sec(time) + seconds
    new_time = sec_to_time(total_sec_change_time)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
