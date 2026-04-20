import sys

nums = []

for line in sys.stdin:
    nums.append(int(line))
    nums.sort()

    n = len(nums)
    if n % 2 == 1:
        print(nums[n//2])
    else:
        print((nums[n//2 - 1] + nums[n//2]) // 2)