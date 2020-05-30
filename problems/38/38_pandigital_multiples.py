from euler.utils.timing import print_exec_time

def is_pan(snum: str) -> bool:
    if not len(snum) == 9:
        return False
    nums = set()
    for x in snum:
        if x == "0":
            return False
        if not x in nums:
            nums.add(x)
        else:
            return False
    return True

def find_answer():
    answer = ""
    for x in range(2, 9999):
        num = ""
        multiplier = 1
        while len(num) < 9:
            num += str(x * multiplier)
            multiplier += 1
        if len(num) != 9:
            continue
        else:
            if is_pan(num):
                answer = num
                # print(f"{x} => {num}")
    print(f"Answer: {answer}")

print_exec_time(find_answer)