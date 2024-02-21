from datetime import *

def Diff(a, b):
    diff_seconds = (a - b).total_seconds()
    print("Difference in seconds:", diff_seconds)
    return diff_seconds
a = datetime(2024, 2, 15, 0, 0)
b = datetime(2024, 2, 15, 0, 0)
Diff(a, b)
