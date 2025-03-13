import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    time_suffix = s[8:len(s)]
    hour = int(s[0:2])
    minute = s[3:5]
    seconds = s[6:8]
    
    if time_suffix == 'PM':
        # 12PM edge case
        if hour == 12:
            return f"{hour:02}:{minute}:{seconds}"
        
        # conversion
        military_hour = 12 + hour
        return f"{military_hour}:{minute}:{seconds}"        
    
    elif time_suffix == 'AM':
        # midnight edge case
        if hour == 12:
            military_hour = "00"
            return f"{military_hour}:{minute}:{seconds}"
    
    # if all else fails, it's AM and no conversion is needed
    return f"{hour:02}:{minute}:{seconds}"

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)