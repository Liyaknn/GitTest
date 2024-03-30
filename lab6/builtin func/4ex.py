import time
import math

def delayed_square_root(milliseconds):
    seconds = milliseconds / 1000
    time.sleep(seconds)
    result = math.sqrt(25100)
    print( result)

delayed_square_root(2123)  