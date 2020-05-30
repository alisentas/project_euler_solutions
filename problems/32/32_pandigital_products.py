from euler.utils.timing import print_exec_time

def is_pan(num: int) -> bool:
    snum = str(num)
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
    wantedNums = set()
    for i in range(2, 10):
        for j in range(i, 9999):
            num = str(i) + str(j) + str(i * j)
            if not len(num) == 9:
                continue
            elif is_pan(num):
                    print(f"{i} x {j} = {i*j}")
                    wantedNums.add(i * j)
    for i in range(11, 999):
        for j in range(i, 999):
            num = str(i) + str(j) + str(i * j)
            if not len(num) == 9:
                continue
            elif is_pan(num):
                    print(f"{i} x {j} = {i*j}")
                    wantedNums.add(i * j)

    print(f"Found: {len(wantedNums)} numbers")
    print(f"Sum (answer): {sum(wantedNums)}")

print_exec_time(find_answer)