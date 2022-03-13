class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, node):
        if self.value > node.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)#insert的时候就是对比两个节点的值，如果小，就看看左边有没有子节点，如果没有，就插入左边，如果有，就调用左边子节点的insert
        elif self.value < node.value:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)


def level_order(root):#思路是：把上一层的放到一个数组里面，然后每次都pop(0)，把上一层弹出来，然后把他的子节点塞进去，然后打印弹出来的那个，通过length来控制他弹出来几个元素
    if root is None:
        return
    q = [root]
    while len(q) != 0:
        length = len(q)
        for i in range(length):
            r = q.pop(0)
            if r.left is not None:#r.left获取r的左节点
                q.append(r.left)#每次都吐出来，然后塞进去左右子节点
            if r.right is not None:
                q.append(r.right)
            print(r.value, end=' ')
        print()


if __name__ == '__main__':#用Node(value)来新建一个节点
    root = Node(int(input()))#第一个节点就是root = Node(第一次输入的值）
    while True:
        try:#检测输入是否完成
            root.insert(Node(int(input())))
        except EOFError:#ACM停止输入的时候会报的错
            break#看看是否输入结束
        except Exception:
            break
    level_order(root)