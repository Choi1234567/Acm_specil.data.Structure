import math#修复最小堆，打印交换值


def heap(lst, l, res):
    depth = int(math.log2(l))#高度公式
    for i in range(0, depth):#最后一层因为没有子节点交换所以不用管
        for j in range(2 ** depth - 2, 2 ** i - 2, -1):#从倒数第二行的最后一个，交换子节点，一直交换到第0个（2 ** 0 -2 = -1，但是是在range里面，所以实际上循环到0就结束了）
            exchange(lst, l, res, j)
    return res


def exchange(lst, l, res, i):#lst数组，l是长度，res是结果，i是要交换的那个节点
    left = 2 * i + 1
    right = 2 * i + 2

    if right < l and lst[right] < lst[left]:#先比较子节点之间的大小，再拿小的那个来比
        if lst[i] > lst[right]:
            lst[i], lst[right] = lst[right], lst[i]
            res.append(str(i) + " " + str(right))
    else:
        if left < l:
            if lst[i] > lst[left]:
                lst[i], lst[left] = lst[left], lst[i]
                res.append(str(i) + " " + str(left))


if __name__ == '__main__':
    l = int(input())
    lst = list(map(int, input().split()))
    res = heap(lst, l, [])
    print(len(res))#要打印交换的次数，所以打印了长度
    for i in res:
        print(i)