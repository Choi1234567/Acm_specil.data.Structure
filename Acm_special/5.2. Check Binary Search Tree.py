class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node


def check_BST(node, min_value, max_value):#这个函数，就是遍历每个节点，然后看看这个节点是不是比小于参数里面的最大值，大于参数里面的最小值
    if node is None:#直到检查叶子的左右子节点，都是None，所以返回true
        return True
    if node.value >= max_value or node.value < min_value:
        return False
    return check_BST(node.left, min_value, node.value) and check_BST(node.right, node.value, max_value)
#这个递归左边只变动最小，右边只变动最大值，缩小范围，万一左边比最大值大，或者右边比最小值小那就False了。


if __name__ == '__main__':
    num = int(input())#节点数
    #input例子：4 1 L 意思是4放在第一个节点的右边
    root_value = int(input())
    root = Node(root_value)#访问了class Node类名。
    nodes = [root]#存节点的排序
    res = True
    for i in range(1, num):#第一次输入，已经在前面输入过了，所以range是num而不是num+1
        line = input().split()
        value = int(line[0])
        parent = int(line[1])
        direction = line[2]
        parent_node = nodes[parent - 1]
        node = Node(value)
        if value < parent_node.value and direction == 'L' and parent_node.left is None:
            parent_node.insert_left(node)
        elif value >= parent_node.value and direction == 'R' and parent_node.right is None:
            parent_node.insert_right(node)
        else:
            res = False
            break
        nodes.append(node)
    if res:
        res = check_BST(root, -2 ** 31, 2 ** 31)#题目给的范围
    if res:
        print('YES')
    else:
        print('No')