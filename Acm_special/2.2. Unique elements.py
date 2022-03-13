import collections#counter就是特殊的字典，自动计数

n = input()
counter = collections.Counter(input().split())
count = 0
for i in counter:
    if counter[i] == 1:
        count += 1
print(count)