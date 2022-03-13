def lis(arr):
    max_len = 1
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])#取这三个中较大的一个
    return max_len


if __name__ == '__main__':
    lenth = int(input())
    arr = list(map(int, input().split()))
    print(lis(arr))