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
        if hour == 12:
            return f"{hour:02}:{minute}:{seconds}"
            
        military_hour = 12 + hour
        return f"{military_hour}:{minute}:{seconds}"        
    elif time_suffix == 'AM':
        if hour == 12:
            military_hour = "00"
            return f"{military_hour}:{minute}:{seconds}"
        
    return f"{hour:02}:{minute}:{seconds}"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()