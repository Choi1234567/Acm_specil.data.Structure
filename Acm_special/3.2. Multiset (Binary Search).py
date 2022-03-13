def count(num, arr):#该递归结束条件就是一直二分到最后只有一个元素
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= num:
            start = mid + 1
            if start > end:
                return end + 1
        else:
            if mid == 0:#如果mid==0，那就证明只有一个元素，并且这个元素还大于num，所以return 0
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
        left.append(int(line[0]))#输入的是连续区间段，left是开始的区间，right是区间结尾
        right.append(int(line[1]))
#先排序才能用二分法，二分查找一定是有序的
    left.sort()
    right.sort()
    for i in range(left[0], right[times - 1] + 1):
        ans = count(i, left) - count(i - 1, right)#一个是找到i大于等于left的个数的函数；一个是找到i大于right的个数的函数
        if ans != 0:#如果左右次数相等，那就说明这个数字超过右端点，不存在于这些区间里
            print(i, " ", ans)
#如果一个数字，大于等于左边的数组里面的数字几次，就代表这个数字出现了几次。例如5比1 2 3 4都大，所以出现了4次
#大于等于左边的数组的个数，减去大于右边的数组的次数