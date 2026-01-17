nums = list(map(int, input().split()))
from collections import Counter

n = len(nums) // 2
count = Counter(nums)

for num, freq in count.items():
    if freq == n:
        print(num)
        break
