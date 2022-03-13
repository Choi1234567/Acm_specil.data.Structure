from itertools import combinations  # 我们只要保证，父节点在子节点前面就行


# C(节点数，左子树的节点数) * 左子树的所有情况 * 右子树的所有情况
# 无强制顺序的所有情况是A(x,x)，然后要排除掉a个节点里面的b个有序的情况

def sequences(nums):
    if not nums:
        return 1
    left = [i for i in nums if i < nums[0]]#把小于根节点的，放到left数组；是把大于根节点的放到right数组
    right = [i for i in nums if i > nums[0]]
    return len(list(combinations(nums[:-1], len(left)))) * sequences(left) * sequences(right)
#nums[：-1]  —— 这个是去掉根节点的，因为根节点的顺序是不变的，然后len(list(xxx))，意思是从去掉根节点的数组里面，就是把所有组合变成数组，然后求出len，就是求出所有排列组合
#sequences(left) * sequences(right)，一直递归，直到nums为空
#len(left)，意思是从去掉根节点的数组里面，挑出len(left)个元素重新组合，总共有多少种情况

if __name__ == '__main__':
    print(sequences(list(map(int, input().split()))))
