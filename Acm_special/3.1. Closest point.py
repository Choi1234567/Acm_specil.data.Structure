def get_nearest_point(num, arr, start, end):#写递归的时候要注意递归结束条件
    mid = (end + start) // 2#整除
    if start >= end - 1 or arr[mid] == num:#特殊情况1只剩下一个元素，那么只有这个元素最接近；特殊情况2，arr[mid]刚好等于num
        return arr[mid]
    if arr[mid] > num:
        if arr[mid - 1] == num:
            return arr[mid-1]
        elif arr[mid-1] < num:#这个跟第五行代码形成介值定理
            if arr[mid] - num > num - arr[mid - 1]:
                return arr[mid - 1]
            else:
                return arr[mid]
        else:
            return get_nearest_point(num, arr, start, mid)
    else:
        return get_nearest_point(num, arr, mid, end)


if __name__ == '__main__':
    end = int(input())
    input_arr = list(map(int, input().split()))
    input_arr.sort()
    times = int(input())

    for i in range(times):
        print(get_nearest_point(int(input()), input_arr, 0, end))

#递归主要是两大部分，一个是递归结束条件；一个是不满足递归条件的时候如何进入递归
#而递归结束条件又分成两种，一种是特殊情况，一种是普遍情况
#还有就是，所有递归，其实都可以用非递归的方法循环实现，而且其实会更加省资源，循环会更加省资源，但是递归的代码，更加“优雅”