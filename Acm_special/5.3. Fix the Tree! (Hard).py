class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mid_order(node, lst):#一直遍历左边，并且加到一个栈里面去，如果左边没有子节点了，就弹出来，然后遍历右边
    stack = []
    pos = node
    while pos is not None or len(stack) > 0:
        if pos is not None:#有左边，就一直遍历左边，一直到左边为none，就打印这个节点本身，然后遍历右边，打印的顺序是左，中，右
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()#pop是栈经常用的
            lst.append(pos.value)
            pos = pos.right

#所谓动态规划，就是把前面的一些东西存下来，省去重复计算这些东西的时间，这题就是先算一下第一个元素的递增个数，存起来
def fix_arr(arr):
    max_len = 1#所有最长增长子序列默认为1，就是它本身
    dp = [1] * len(arr)#dp[i]代表，以i结尾的最长递增子序列是几，例如dp[2] = 2，因为有两个元素1，2，递增，所以是2
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and arr[i] - arr[j] >= i - j and arr[i] >= i + 1 and arr[j] >= j + 1:#相邻差距要大于1，第n个要大于等于n
                dp[i] = max(dp[i], dp[j] + 1)#dp[i] 或者dp[j] + 1，对比一下看看谁更大
        max_len = max(max_len, dp[i])
    return len(arr) - max_len#得出需要改变对节点


if __name__ == '__main__':
    f = open("fix.out", "w")#输出文件
    file = open("fix.in")#输入读文件
    i = int(file.readline())#打开这两个文件，一行一行读
    try:
        while i != 0:
            lst = []#储存节点
            for j in range(i):
                line = file.readline().split()
                value = int(line[0])
                father = line[1]
                node = Node(value)
                if father != '0':
                    if father[-1] == 'L':
                        lst[int(father[:-1]) - 1].left = node#[a:b]，是指从a到b-1，所以[:-1]是指，从0到-2
                    else:
                        lst[int(father[:-1]) - 1].right = node#father[:-1]指0到倒数第二个
                lst.append(node)
            arr = []
            mid_order(lst[0], arr)
            print(fix_arr(arr), file=f)#计算结果通过print地方法写进去fix.out
            i = int(file.readline())
    except EOFError:#防止非正常结束
        pass
    except Exception:
        pass
