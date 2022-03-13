import heapq  # 堆又有一个名字，叫优先队列，他的堆顶，或者说优先队列的第一个元素，永远都是最大值或最小值


# 如果一个数据，里面的最大值经常变化，可以用这种数据结构，因为每次变化，重新选举出新的最大值或最小值的算法复杂度是logn
# 从上往下，削掉一个最大值的时候，算法复杂度也是logn
#一开始的思路是维护两个堆，最大堆和最小堆，但是发现最小值变化不频繁，直接遍历求出即可，无需用堆这个数据结构，后来也发现，也没法维护两个堆，最小堆无法维护
# 反而最大值可以用最大堆更新取出。小根堆里面，我们根本不知道最大值是哪个，只能通过遍历的方法才能知道最大值在哪里，
# 既然遍历了，算法复杂度又变成O(n)了，没有用堆的意义。所以从这个角度，也没法用小根堆
def process(lst, l):#lst数组，l数组长度
    if l == 0:#特殊情况
        return 0
    count = 0
    max_pq = []
    min_num = lst[0]
    for i in lst:#用最普遍的方法求出最小值,Find the minimum value by the most general method
        if i < min_num:
            min_num = i
        heapq.heappush(max_pq, -i)#每次遍历得时候，都把-i，用堆得形式，放到max_pq这个数组里面
    max_num = -max_pq[0]#这个函数，默认是构建小根堆得，所以我们用-i，就变成构建了大根堆了
    if max_num == min_num:
        return 0
    while min_num < max_num:
        if max_num > 2 * min_num:#最大值大于2*min_num的时候，相减，最小值不会变，最大值小于2*最小值的时候，相减，最小值会变化
            c = max_num // min_num - 1
            num = max_num - c * min_num
            count += c
            heapq.heapreplace(max_pq, -num)#取出最大值，然后把num塞堆里
            max_num = -max_pq[0]
        else:#max_num <= 2 * min_num的时候，最小值也发生变化了
            num = max_num - min_num
            min_num = num
            count += 1
            heapq.heapreplace(max_pq, -num)#塞到堆里
            max_num = -max_pq[0]##重新取出新的最大值
    return count


if __name__ == '__main__':
    l = int(input())
    lst = list(map(int, input().split()))
    print(process(lst, l))
