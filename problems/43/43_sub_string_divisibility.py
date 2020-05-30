from itertools import permutations

from euler.utils.timing import print_exec_time

def find_answer():
    nums = []
    for x in permutations([0,1,2,3,4,5,6,7,8,9]):
        if x[0] == 0:
            continue
        else:
            # I'm not very proud of this pyramid
            if (x[1] * 100 + x[2] * 10 + x[3]) % 2 == 0:
                if (x[2] * 100 + x[3] * 10 + x[4]) % 3 == 0:
                    if (x[3] * 100 + x[4] * 10 + x[5]) % 5 == 0:
                        if (x[4] * 100 + x[5] * 10 + x[6]) % 7 == 0:
                            if (x[5] * 100 + x[6] * 10 + x[7]) % 11 == 0:
                                if (x[6] * 100 + x[7] * 10 + x[8]) % 13 == 0:
                                    if (x[7] * 100 + x[8] * 10 + x[9]) % 17 == 0:
                                        num = "".join(str(a) for a in x)
                                        print(f"Num: {num}")
                                        nums.append(int(num))
    print(f"Answer: {sum(nums)}")

print_exec_time(find_answer)