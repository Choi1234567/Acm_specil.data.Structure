n = int(input())#动态规划
curr = 1
last = 1
for n in range(3, n + 1):
    last, curr = curr, curr + last
print(curr)