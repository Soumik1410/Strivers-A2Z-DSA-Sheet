from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    maxi = 0
    sum = 0
    i = 0
    j = 1
    while j < len(prices):
        if prices[j] - prices[i] > maxi:
            maxi = prices[j] - prices[i]
        if prices[j] < prices[i]:
            i = j
        j += 1
    return maxi
