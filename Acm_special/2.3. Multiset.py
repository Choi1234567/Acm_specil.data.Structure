def count(num, arr):#Already in order
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= num:
            start = mid + 1
            if start > end:
                return end + 1
        else:
            if mid == 0:
                return 0
            if arr[mid - 1] > num:
                end = mid - 1
            else:
                return mid
    return 0


if __name__ == '__main__':
    times = int(input())
    left = []
    right = []

    for i in range(times):
        line = input().split()
        left.append(int(line[0]))
        right.append(int(line[1]))

    left.sort()
    right.sort()
    for i in range(left[0], right[times - 1] + 1):#下标应该减1，The subscript should be minus 1
        ans = count(i, left) - count(i - 1, right)#count(a, arr)是找出arr里面，小于等于a的数字的个数，a > b 等价于 a-1 >= b
        if ans != 0:
            print(i, " ", ans)