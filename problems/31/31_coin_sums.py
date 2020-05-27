from euler.utils.timing import print_exec_time

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def count(target: int, coinIndex: int) -> int:
    if target == 0:
        return 1
    elif target < 0 or coinIndex < 0:
        return 0

    return count(target, coinIndex - 1) + count(target - coins[coinIndex], coinIndex)

def find_answer():
    print(count(200, 7))

print_exec_time(find_answer)