s = input().strip()
p = input().strip()

from collections import Counter

len_p = len(p)
count_p = Counter(p)
count_s = Counter(s[:len_p])
result = []

if count_s == count_p:
    result.append(0)

for i in range(len_p, len(s)):
    count_s[s[i]] += 1
    count_s[s[i - len_p]] -= 1
    if count_s[s[i - len_p]] == 0:
        del count_s[s[i - len_p]]
    if count_s == count_p:
        result.append(i - len_p + 1)

print(result)
