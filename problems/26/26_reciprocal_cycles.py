import numpy as np
from euler.utils.timing import print_exec_time

def find_cycle(num: int) -> str:
    """ Finds the cycle (if any) in 1 / num """
    dividends = [] # This will hold the dividends in the cycle
    cycle = "" # This will hold the current cycle
    
    dividend = 10 # number to divide the number by
    while True:
        if dividend < num:
            dividend *= 10
        elif dividend > num:
            if dividend not in dividends:
                dividends.append(dividend)
                quotient, remainder = dividend // num, dividend % num
                cycle += str(quotient)
                if dividend % num == 0:
                    return ""
                else:
                    dividend = remainder
            else:
                return cycle
        else:
            return cycle

def find_answer():
    cycle_lengths = [len(find_cycle(x)) for x in range(2, 1000)]
    biggest_idx = np.argmax(cycle_lengths)
    
    # 2 is added because range starts from 2 and not 0 so for example the 10th element in the list would be 12
    print(f"{2 + biggest_idx} has the biggest cycle with {cycle_lengths[biggest_idx]} elements.")
    
print_exec_time(find_answer)
