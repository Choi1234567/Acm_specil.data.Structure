from math import log
#高度为h，节点数为n的ASL，拆成高度为h-1，然后左边为x，右边为n - x -1的两颗树，
# 分别求出这两棵树的所有情况，然后相乘，得出两边高度相等的情况下，
# 这个树有多少情况，再拆成左边为x，高度为h-2，右边为n - x - 1，高度为h的两棵树，
# 分别求出这两棵树的所有情况，然后相乘，考虑到还存在右边为h-2,左边为h-1，所以这种情况下，还要乘以2
#那么高度为h-1，节点数为n的情况有哪些呢？就继续拆，因为我们用for循环从2，2，0开始计算
n = int(input())#输入节点
max_height = int(1.45 * log(n + 2, 2)) + 1
min_height = int(log(n + 1, 2))#高度范围，题目有给


vsl_list = [[0 for i in range(max_height)] for j in range(n + 1)]
vsl_list[0][0] = 1#第一个位置是节点，第二个是高度
vsl_list[1][1] = 1
for i in range(2, n + 1):#i   -> 节点数   j -> 高度   k->左子节点的数
    for j in range(2, max_height):#前面计算的时候已经+1了
        for k in range(i):#左边节点数i-k-1，右边是k
            vsl_list[i][j] = (vsl_list[i][j] + vsl_list[i - k - 1][j - 1] * vsl_list[k][j - 1])#最后的参数是左右子树的情况，把节点为n-1，高度为h-1，并且左右子树相等的所有情况都列出来
            vsl_list[i][j] = (vsl_list[i][j] + 2 * vsl_list[i - k - 1][j - 2] * vsl_list[k][j - 1])#乘以2是考虑左低右高，右高左低两种情况
#第一种是左右一样高，第二种是左右不一样高，所以要乘以2

ans = 0
for i in range(min_height, max_height):#把节点固定，高度可能的范围情况，加起来
    ans += vsl_list[n][i]
print(ans)


#AVL树，就是左右子树的高度差，不能大于1，之所以要搞这个平衡二叉树，是为了保证，查询的时候，算法复杂度可以稳定为logn