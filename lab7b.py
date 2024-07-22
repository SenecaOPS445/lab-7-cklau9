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
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    #[ insert python code here to check for minute and second 
    #[ attribute here, and carry over when necessary
    #[
    if sum.second >= 60: # Check the sum.second greater than 60 seconds
        sum.second = sum.second - 60 # Adjust sum.second shall minus 60
        sum.minute = sum.minute + 1 # Adjust sum.minute by add 1
    if sum.minute >= 60: # Check the sum.minute greater than 60 minutes
        sum.minute = sum.minute - 60 # Adjust sum.minute shall minus 60
        sum.hour = sum.hour + 1 # Adjust sum.hour by add 1
    return sum

def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
    
    # calculate the time if seconds and/or minute >= 60 
        while time.second >= 60:
            time.second -= 60
            time.minute +=1
        while time.minute >= 60:
            time.minute -= 60
            time.hour += 1
        
        # calculate the time if seconds and/or minute <= 0 
        while time.second < 0: # Do while loop to handle negative second input 
            time.minute -= 1 # Deduct 1 minute, then add 60 seconds
            time.second += 60 # New second add 60 seconds
        while time.minute < 0: # Do while loop while negative minute generated
            time.hour -= 1 # Deduct 1 hr, then add 60 minutes
            time.minute += 60
 
    return None

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
