class Tree:#一开始用对象来初始化线段树，后面超时了，就改成用数组了，然后忘记把对象改回来了
    def __init__(self, n):
        self.arr = [0] * (4 * n)#所有初始化空数组，然后append的，都可以用这种方法，先初始化

    def add(self, index, pos, left, right, num):## 投num个篮球到index位置的篮筐，index:篮球的编号，pos:线段树数组的位置，left:左端点，right : 右端点，num:篮球的数量
        self.arr[pos] += num
        if left == right:
            return
        mid = (left + right) // 2
        if index <= mid:
            self.add(index, 2 * pos + 1, left, mid, num)
        else:
            self.add(index, 2 * pos + 2, mid + 1, right, num)

    def query(self, l, r, pos, left, right):# 查询从l到r位置有多少个篮球，l,r ：要查询的篮球的左右子端点，pos ：当前节点在线段树数组中的位置，# left,right ：当前节点的左右端点
        if l <= left and r >= right:#递归结束条件是：l比left还左了；r比right还右了，证明这段区间，已经完全被l和r包裹了
            return self.arr[pos]
        mid = (left + right) // 2
        left_value = 0
        right_value = 0
        if mid >= l:#判断一下是不是在左右两边，然后加起来，如果只有一边的画，就只返回一边的就行了，因为另一边初始化是0
            left_value = self.query(l, r, 2 * pos + 1, left, mid)
        if mid < r:
            right_value = self.query(l, r, 2 * pos + 2, mid + 1, right)
        return left_value + right_value


if __name__ == '__main__':
    baskets, num = map(int, input().split())#baskets - 篮筐数, num - 接下来投几次篮球
    tree = Tree(baskets)
    for i in range(num):
        p, k, l, r = map(int, input().split())
        tree.add(p - 1, 0, 0, baskets - 1, k)#因为数组是0开始的，编号是1开始的，所以这里p和basket都减一了
        print(tree.query(l - 1, r - 1, 0, 0, baskets - 1))