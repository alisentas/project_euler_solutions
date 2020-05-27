import timeit
from typing import Callable

def print_exec_time(function: Callable) -> None:
    start = timeit.default_timer()
    function()
    stop = timeit.default_timer()
    print(f'Execution time: {stop - start:.4f} seconds.') 



