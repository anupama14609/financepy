import numpy as np 
import pandas as pd 

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1

        if col < -requirement:
            return -1
    return 0 

buy_sell_hold()
