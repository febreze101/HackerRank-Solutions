#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def circular_sliding_window(arr, win_size):
    arr_len = len(arr)
    result = []
    
    for curr_loc in range(arr_len):
        window = [arr[(curr_loc + win_idx) % arr_len] for win_idx in range(win_size)] # wrap around
        result.append(window)
        
    return result

def miniMaxSum(arr):
    # Write your code here    
    
    win_arrays = circular_sliding_window(arr, 4)
    
    min_sum = sum(win_arrays[0])
    max_sum = sum(win_arrays[0])
    for sub_arr in win_arrays:
        
        curr_min_sum = sum(sub_arr) 
        if curr_min_sum <= min_sum:
            min_sum = curr_min_sum
        
        curr_max_sum = sum(sub_arr) 
        if curr_max_sum >= max_sum:
            max_sum = curr_max_sum
            
    print(f"{min_sum} {max_sum}")
        
         

if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
