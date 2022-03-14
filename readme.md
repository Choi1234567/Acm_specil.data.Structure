# 数据结构作业题解

## 1. 复杂性

---

### 1.1 斐波拉契数列
[原题地址](https://acm.bsu.by/courses/246/problems/4526/)

#### 题意
输入一个数字n，打印出斐波拉契数列的第n个数字

#### 解析
斐波拉契数列的第1和第2个数字，固定是1，所以我们从3开始循环，如下代码，如果n为1或者2，那么直接跳过循环打印curr，也就是1；如果n大于等于3，就会进入循环，每次循环，last都会变成curr，而curr则会变成last + curr：


| n | last | curr |
| ------- | ------- | ------|
| 1        |  1       |  1     |
| 2        |  1       |  1     |
| 3        |  1       |  1 + 1 = 2    |
| 4        |  2       |  2 + 1 = 3     |
| 5        |  3       |  3 + 2 = 5     |
| 6        |  5       |  5 + 3 = 8    |
| ...        |  ...       |  ...     |


``` python
n = int(input())
curr = 1
last = 1

# 从3开始，如果小于3，那就直接跳过循环打印1
# 因为range(a,b)实际上是从a开始，b-1结束，所以如果要循环到n，就需要是n + 1 
for n in range(3, n + 1):
    last, curr = curr, curr + last
print(curr)

```

---


### 1.2 查找数字
[原题地址](https://acm.bsu.by/courses/246/problems/4527/)

#### 题意
查找一个数字是否在数组里面。
输入：第一行，数组的长度；第二行，数组，第三行，输入一个数字n，代表接下来还要输入n个数字来查询；从第四行开始，总共会输入n个数字，每输入一个数字，就去查找数组里面有没有这个数字，如果有，则打印"FOUND"，否则打印"MISSED"

#### 解析
直接用语句 a in b ：如果a在数组b里面，就返回True，否则返回False

``` python
i = input()
line = input()
l = line.split()
m = int(input())
count = 0
while count < m:
    count += 1
    if input() in l:
        print("FOUND")
    else:
        print("MISSED")

```
---
## 排序

---
### 2.1 合并数组
[原题地址](https://acm.bsu.by/courses/246/problems/4544/)

#### 题意
合并两个**有序**数组
输入：第一行，数组a的长度；第二行，数组a；第三行，数组b的长度；第四行，数组b

输出：合并后的数组

#### 解析
如果arr[i]小于等于arr1[index],就把arr2[i]插入到ans[index+1]的位置；否则arr2遍历到下一个元素，继续对比

假设a 为[1,5,7,9] b为 [3,8,10,11]例

直接从循环开始看：

| ans | index | a[index] | i | b[i] | 
| ------- | ------- | ------- | ------- | ------- |
| 1 5 7 9 |    0    |  1      | 0       | 3       |
| 1 5 7 9 |    1    |  5      | 0       | 3       |
| 1 3  5 7 9 |    1  |  5      | 1      | 8       |
| 1 3 5 7 9 |    2    |  7      | 1     | 8       |
| 1 3 5 7 9 |    3    |  9      | 1     | 8       |
| 1 3 5 7 8 9 |    3    |  9    | 2     | 10       |
| 1 3 5 7 8 9 |    3    |  9    | 3     | 11       |
| 1 3 5 7 8 9 10 11 |    3    |  9    | -     | -       |


``` python
def merge(arr1, arr2):
    ans = arr1.copy()
    index = 0
    for i in range(0, len(arr2)):
        while index < len(arr1):
			# 如果arr[i]小于等于arr1[index],就把arr2[i]插入到ans[index+1]的位置；否则arr2遍历到下一个元素，继续对比
            if arr2[i] <= arr1[index]:
                ans.insert(index + i, arr2[i])
                break
            else:
                index += 1
        else:
			# 如果arr1已经遍历完了，那代表arr2剩下的元素都比arr1大，所以直接把剩下的插入就行了
            ans = ans + arr2[i:]
            break
    return ans


if __name__ == "__main__":
    input()
    arr1 = list(map(int, input().split()))
    input()
    arr2 = list(map(int, input().split()))
    c = merge(arr1, arr2)
	# map(str,c)，指把数组c的每个元素变成字符串，然后" ".join(map(str,c),指把数组里面的每个元素用空格连接起来
    print(" ".join(map(str, c)))
```
---
### 2.2 维一的元素
[原题地址](https://acm.bsu.by/courses/246/problems/4545/)

#### 题意
输入：第一行n，第二行，n个元素的数组
输出：该数组中独一无二的元素的个数有多少

#### 解析
利用counter，假设一个数组a = [1,2,3,4,3,2]，那么Counter(a) = [1:1,2:2,3:2,4:1]，自动就算出了每个元素的个数
然后再遍历这个counter的key，如果counter[key]=1，那么就把目前独一无二的元素的个数加一，最后遍历完了打印出来即可

引申链接：[Counter文档](http://www.pythoner.com/205.html)


``` python
import collections

n = input()
counter = collections.Counter(input().split())
count = 0
for i in counter:
    if counter[i] == 1:
        count += 1
print(count)
```
---

### 2.3 多集合
[原题地址](https://acm.bsu.by/courses/246/problems/4546/)

#### 题意
输入：第一行，数字n；接下来的n行：输入两个数字，分别代表数组的开始和结尾

输出：n个数组的并集的每个元素的个数

例子：比如分别输入了 

1 5-代表着数组[1,2,3,4,5]

2 4-代表着数组[2,3,4]

7 9-代表这数组[7,8,9]

最终形成的数组的并集就是[1,2,2,3,3,4,4,5,7,8,9]

然后打印出每个元素在这个并集里面出现的个数
1 1

2 2

3 2

4 2

5 1

7 1

8 1

9 1



#### 解析
见3.2


---
## 3. 二分查找

---
### 3.1 最接近的点
[原题地址](https://acm.bsu.by/courses/246/problems/4551/)

#### 题意
输入：第一行n;第二行n个元素的数组;第三行m，接下来的m行输入：任意一个数字

输出：接下来m行每次输入一个数字，都要返回数组里面跟这个数字最接近（即绝对值最小）的数字

例子：
数组：-7 3 8 12 -3 -10

如果输入5，则输出3

输入9，输出8

输入-3，输出-3

输入10，输出8或者12任一都行

#### 解析
先把数组a排序

然后利用二分法查找a[i] > x 且 a[i - 1] < x的位置，然后找到a[i] - x 和 a[i - 1] - x的绝对值较小的那个

比如上面那个例子，排序后变成了 -10 -7 -3 3 8 12，数组里面相邻的两个数，中间的数字，肯定是跟这两个数字之一最接近，
比如 5\6\7三个数字再3和8之间，那肯定离这几个数字最接近的数字要么是3要么是8

``` python
def get_nearest_point(num, arr, start, end):
    mid = (end + start) // 2
	# 递归结束条件：start >= end-1代表这个区间里面只有一个数字了；arr[mid] == num，代表最接近的数字已经找到了
    if start >= end - 1 or arr[mid] == num:
        return arr[mid]
		
	#如果中间的数字大于num
    if arr[mid] > num:
		# 如果前面一个数字小于num，那就已经找到最接近的数字了
        if arr[mid - 1] == num:
            return arr[mid-1]
		# 如果前面一个数字小于num，当前数字大于num，那最接近的数字就在这两个数字之间了，所以求两个绝对值更少的那个就行了
        elif arr[mid-1] < num:
            if arr[mid] - num > num - arr[mid - 1]:
                return arr[mid - 1]
            else:
                return arr[mid]
        else:
			#如果当前数字大于num，前一个数字也大于num，那证明要找的在数组的左半边
            return get_nearest_point(num, arr, start, mid)
    else:
		#如果当前数字小于num，那证明要找的在数组的右半边
        return get_nearest_point(num, arr, mid, end)


if __name__ == '__main__':
    end = int(input())
    input_arr = list(map(int, input().split()))
    input_arr.sort()
    times = int(input())

    for i in range(times):
        print(get_nearest_point(int(input()), input_arr, 0, end))
```
---
### 3.2 多集
[原题地址](https://acm.bsu.by/courses/246/problems/4552/)

#### 题意
**同2.3，但是要用二分法来解决**

输入：第一行，数字n；接下来的n行：输入两个数字，分别代表数组的开始和结尾

输出：n个数组的并集的每个元素的个数

例子：比如分别输入了 

1 7 - 代表数组 1 2 3 4 5 6 7

2 7 - 代表数组 2 3 4 5 6 7

3 6 - 代表数组 3 4 5 6

4 6 - 代表数组 4 5 6

最终形成的数组的并集就是1 2 2 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7

然后打印出每个元素在这个并集里面出现的个数
1 1

2 2

3 3

4 4

5 5

6 5

7 2

#### 解析
以上面的例子为例：

把左边的数字放到一个数组里面  1 2 3 4
把右边的数字放到一个数组里面  7 7 6 6
如果一个数字，大于等于左边的数组里面的数字几次，就代表这个数字出现了几次。

比如1，只大于等于1，所以出现了1次；

3，大于等于1,2,3，所以出现了3次，

5，大于等于1,2,3,4，所以出现了4次

但是7，也是大于等于1,2,3,4，却只出现了两次，因为7大于右边的数组里面的数字两次了，所以还要减去2，所以只出现了两次

总结而言，就是左边数组中小于等于该数字的次数，减去右边小于该数字的次数，就是这个数字最终出现的次数

所以这就是个二分法的问题了，先把左右数组排序，然后用类似3.1的方法，查找数组中当前位置i小于等于该数字；并且位置i + 1的数字大于该数字，
就代表有i个数字小于等于该数字



``` python
# 二分法查找arr中小于等于num的数字有多少
def count(num, arr):
    start = 0
    end = len(arr) - 1
	
	# start和end不断逼近，直到start > end的时候，就代表这个数组用二分法切完了，结束循环	
    while start <= end:
        mid = (start + end) // 2
		
        if arr[mid] <= num:
			# 这时候start 变成了mid + 1，即下一次循环变成了mid + 1 到 end之间的区间了 
            start = mid + 1			
            if start > end:
                return end + 1
        else:
            if mid == 0:
                return 0
			# 如果arr[mid] > num ，且 arr[mid - 1] 大于num，那下一次循环就变成了start 到 mid - 1之间的区间了
            if arr[mid - 1] > num:
                end = mid - 1
			# 如果arr[mid] > num, 且 arr[mid - 1] <= num,那就证明有mid个数字小于等于num
            else:
                return mid
    return 0


if __name__ == '__main__':
    times = int(input())
    left = []
    right = []

    for i in range(times):
        line = input().split()
        left.append(int(line[0]))
        right.append(int(line[1]))
	
	# 先排序才能用二分法
    left.sort()
    right.sort()
    for i in range(left[0], right[times - 1] + 1):
		# 因为要减去右边小于该数字的个数，但是count是查找小于等于某数字的个数，所以这里用了i - 1
		# 即 i <= a 等价于 i - 1 < a
        ans = count(i, left) - count(i - 1, right)
        if ans != 0:
            print(i, ans)
```
---

## 4.堆

---
### 4.1 收集雕像
[原题地址](https://acm.bsu.by/courses/246/problems/4554/)

#### 题意
输入：第一行输入数字n,k；第二行输入有n个元素的数组

输出：输出这个数组包含从1到k的所有元素的子区间的和

比如数组是1 2 6 3 3 1，k是3
那么包含1到3的子区间有  1 2 6 3； 2 6 3 3 1，和分别是12和15，所以打印12

#### 解析
**尚未解决**

``` python
if __name__ == '__main__':
    length, num = map(int, input().split())
    price = total_price = stack = lift = right = 0
    arr_sign = [0] * (num + 1)
    arr = list(map(int, input().split()))
    while lift < length - num + 1:
        if right < length and stack < num:
            if arr[right] <= num and arr_sign[arr[right]] == 0:
                stack += 1
                arr_sign[arr[right]] += 1
            elif arr[right] <= num and arr_sign[arr[right]] > 0:
                arr_sign[arr[right]] += 1
            price += arr[right]
            right += 1
        elif right >= length and stack < num:
            break
        else:
            if price < total_price or total_price == 0:
                total_price = price
            if arr[lift] <= num and arr_sign[arr[lift]] == 1:
                stack -= 1
                arr_sign[arr[lift]] -= 1
            elif arr[lift] <= num and arr_sign[arr[lift]] > 1:
                arr_sign[arr[lift]] -= 1
            price -= arr[lift]
            lift += 1

    print(total_price)
```
---
### 4.2 数字游戏
[原题地址](https://acm.bsu.by/courses/246/problems/4555/)

#### 题意
输入：第一行，数字n；第二行，有n个数字的数组

输出：循环拿数组里面的最大的元素，减去最小的元素；并且用这个差替换这个最大的元素，一直到每个元素都一样大时，打印出一共要减多少次

例子：

9 6 3 2

第一次，9 - 2 = 7，数组变成了 7 6 3 2

第二次，7 - 2 = 5，数组变成了 5 6 3 2

第三次，6 - 2 = 4，数组变成了 5 4 3 2

第四次，5 - 2 = 3，数组变成了 3 4 3 2

第五次，4 - 2 = 2，数组变成了 3 2 3 2

第六次，3 - 2 = 1，数组变成了 1 2 3 2

第七次，3 - 2 = 1，数组变成了 1 2 1 2

第八次，2 - 1 = 1，数组变成了 1 1 1 2

第九次，2 - 1 = 1，数组变成了 1 1 1 1

最终输出9

#### 解析
在最小值没有变的时候，不管减的顺序怎么变化，都不影响结果，所以遍历这个数组，只要不是最小的数字，都直接减到刚好大于等于这个最小值位置，
比如不用 9 - 2 = 7， 7 - 2 = 5， 5 - 2 = 3,直接 9 - 6 = 3，然后记下来9减了三次即可。

比如上面的例子，一次循环过后，就变成了 3 2 3 2，然后 9 6 3 分别减了 3 2 0次，所以现在总共减了 5次，
然后当前最大值减去最小值，3 - 2 = 1，变成了1 2 3 2，然后再循环用上面的方法即可。

我们可以用大根堆的方法来实现，每次拿出堆顶的最大值:

如果这个最大值大于2乘以最小值，则通过上面的方法减去最小值（max - (max//min-1) * min），
然后把这个最大值从堆顶移除，然后把差放到堆里面形成新的堆；

如果这个最大值，小于2乘以最小值，则用最大值减最小值，然后把这个最大值从堆顶移除，然后把差放到堆里面形成新的堆；并且同时把这个差变成最小值。

一直循环，直到最大值=最小值为止

``` python
import heapq


def process(lst, l):
    if l == 0:
        return 0
    count = 0
    max_pq = []
    min_num = lst[0]
    for i in lst:
        if i < min_num:
            # 求出最小值
            min_num = i
        # 因为这个函数是构建小根堆，所以我们这里用-i，这样形成了一个是纯负数的小根堆，绝对值最大的在堆顶
        heapq.heappush(max_pq, -i)
    # 因为存进去是负数，所以在前面加上一个减号，就变回正数了
    max_num = -max_pq[0]
    if max_num == min_num:
        return 0
    # 一直循环，直到最大值大于等于最小值为止
    while min_num < max_num:
        if max_num > 2 * min_num:
            c = max_num // min_num - 1
            num = max_num - c * min_num
            count += c
            # 取出最大值，然后把num塞到堆里
            heapq.heapreplace(max_pq, -num)
            # 取出新的最大值
            max_num = -max_pq[0]
        else:
            num = max_num - min_num
            # 最小值变更
            min_num = num
            count += 1
            # 取出最大值，然后把num塞到堆里
            heapq.heapreplace(max_pq, -num)
            # 取出新的最大值
            max_num = -max_pq[0]
    return count


if __name__ == '__main__':
    l = int(input())
    lst = list(map(int, input().split()))
    print(process(lst, l))
```
---
### 4.3 修复[小根堆](https://baike.baidu.com/item/%E6%9C%80%E5%B0%8F%E5%A0%86/9139372?fromtitle=%E5%B0%8F%E6%A0%B9%E5%A0%86&fromid=4633461&fr=aladdin)
[原题地址](https://acm.bsu.by/courses/246/problems/4556/)

#### 题意
输入：第一行数字n，第二行，n个元素的数组
输出：交换数组中的元素，要求每次交换的元素必须是数组的第i和第2i + 1个元素或者第i 和第 2i + 2个元素；一直交换，
直到所有的元素都满足a[i] < a[2i + 1] 且a[i] < a[2i +2]，然后打印出交换的次数和每次交换的元素的位置

说人话版本：

数组 7 6 5 4 3 2 1，其实可以变成一个堆：

				7
		
		6	 		5
	
	4		3	2		1

每次只能交换第i和第2i + 1个元素或者第i 和第 2i + 2个元素，就是指只能交换父子节点，比如a[0]只能和a[1]\a[2]交换，即，7只能和6或者5交换；
a[2]只能和a[5]\a[6]交换，5只能和2、1交换，交换的结果要求a[i] < a[2i + 1] 且a[i] < a[2i +2]，意思就是父节点只能比子节点小

#### 解析

从倒数第二层的节点开始交换，然后先对比倒数第二层的两个子节点谁小，然后把小的那个节点跟父节点交换，以此循环即可：

上面的树第一次交换，5的两个子节点，1比2小，所以交换1和5

				7
		
		6	 		1
	
	4		3	2		5

第二次交换，6的两个子节点，3比4小，所以交换3和6

				7
		
		3	 		1
	
	4		6	2		5

第三次交换，7的两个子节点，1比3小，所以交换1和7

				1
		
		3	 		7
	
	4		6	2		5

现在根节点已经是最小的节点了，可以不用变了，接下来又重新从倒数第二层开始交换：

第四次交换，7的两个子节点，2比5小，所以交换2和7

				1
		
		3	 		2
	
	4		6	7		5

3的两个子节点都比3大，所以小根堆已经构建完成了（可以验算一下，是不是对于每个元素a[i]，都满足a[i] < a[2i + 1] 且a[i] < a[2i +2]），
总共交换了4次，所以输出：

4

2 6

1 4

0 2

2 5




``` python
import math


def heap(lst, l, res):
	# n个节点的堆的高度为 log2(n)
    depth = int(math.log2(l))
    for i in range(0, depth):
		# 从 l//2+1开始循环，即倒数第二层的最后一个节点，循环到 2 ** i - 1的节点
		# 比如i一开始是0，所以第一次内循环，就是从倒数第二层的最后一个节点，循环到根节点，这时候根节点已经固定可以不用变了
		# 然后i变成1，从倒数第二层的最后一个节点循环到arr[1]，即第一层的第一个节点，这时候根节点和第一层已经固定了
		# 然后i变成2，从倒数第二层的最后一个节点循环到arr[3]，即第二层的第一个节点，这时候根节点和第一、二层也固定了
		# 以此类推，每次循环，都会把第i层固定，直到i = depth - 1为止（因为叶子节点不用管了），所有的就都固定了
        for j in range(l//2 + 1, 2 ** i - 2, -1):
            exchange(lst, l, res, j)
    return res


def exchange(lst, l, res, i):
	# 左右子节点的下标
    left = 2 * i + 1
    right = 2 * i + 2
	
	# 如果右节点大于数组长度了，那这个节点不存在了，所以肯定不交换了
	# 为什么这里不判断左节点存不存在呢？ 因为如果右节点都存在了，那左节点肯定存在
	# 如果右节点小于数组长度，并且右边的数字小于左边的数字
    if right < l and lst[right] < lst[left] :
		# 如果当前节点小于右几点，那就交换，并且把这次交换的记录存到res里
        if lst[i] > lst[right]:
            lst[i], lst[right] = lst[right], lst[i]
            res.append(str(i) + " " + str(right))
    else:
		# 如果左节点存在，并且当前节点小于左节点，就交换，并且存到res里
        if left < l:
            if lst[i] > lst[left]:
                lst[i], lst[left] = lst[left], lst[i]
                res.append(str(i) + " " + str(left))


if __name__ == '__main__':
    l = int(input())
    lst = list(map(int, input().split()))
    res = heap(lst, l, [])
    print(len(res))
    for i in res:
        print(i)
```
---
## 5. [二分查找树](https://zhuanlan.zhihu.com/p/133324642)
**二分查找树：指树的每个节点的所有左边子节点都比该节点小，所有右边子节点都比该节点大**

---

### 5.1 构建二分查找树
[原题地址](https://acm.bsu.by/courses/246/problems/4557/)

#### 题意
输入一串数字，按照输入的数字的顺序，构建一个二分查找树，并且按从上到下，从左到右的顺序打印出来

比如按顺序输入：

5 - 成为根节点

        5

2 - 比5小，所以，所以成为5的左边子节点

        5
    2

4 - 比5小，所以在5的左边，5的左边是2，比2大，所以在2的右边

            5
    2
        4

1 - 比5小，所以在5的左边，5的左边是2，比2小，所以在2的左边

                5
        2
    1       4

8 - 比5大，在5的右边

                5
        2               8
    1       4

7 - 比5大，在5的右边，5的右边是8，比8小，在8的左边
        
                5
        2               8
    1       4       7

输入完成之后，最后按照从上到下、从左到右打印这个树即可：

5

1 8

1 4 7


#### 解析
这题主要是分两个部分，一个是构建树，一个是打印树；
构建树的话，直接递归插入即可，根据大小，判断在左边还是右边，然后再看看做左右边是不是为None，
如果为None，就插入到对应位置，如果不为None，就再拿子节点来跟要插入的数字来对比，以此类推
打印树的话，一层一层来，先遍历上一层，然后把上一层的子节点放入数组，然后把上一层打印出来；然后从数组里面拿出子节点，
再把这一层子节点的所有子节点放入数组，然后把这一层打印出来，以此类推

``` python
# 节点对象，包含左边子节点、右边子节点和实际数值三个属性
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    # 循环递归插入，把要插入的节点的node的value跟self的value对比
    # 如果self更大，就判断左边子节点是否为空，如果为空，就把left赋值为node，如果不为空，就继续插入left，直到left为空为止
    # 右边也是一个道理
    def insert(self, node):
        if self.value > node.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        elif self.value < node.value:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

# 打印二分查找树
def level_order(root):
    # 如果为none，直接结束
    if root is None:
        return
    # 把当前节点放入临时数组q
    q = [root]
    while len(q) != 0:
        length = len(q)
        # length是当前的q的长度；下面虽然会append子节点进来，但是只遍历完当前的节点就结束了，后面append的不参与遍历
        for i in range(length):
            # 删除数组第一个元素，并且赋值给r
            r = q.pop(0)
            if r.left is not None:
                # 插入刚刚删除的元素的左节点
                q.append(r.left)
            if r.right is not None:
                # 插入刚刚删除的元素的右节点
                q.append(r.right)
            # 打印刚刚删除的元素，并且以空格为结尾
            print(r.value, end=' ')
        # 换行
        print()
    # 通过以上的代码，每次都只遍历一层的节点并且打印出来，然后把左右子节点放进去q，进行新的遍历，直到q完全为空


if __name__ == '__main__':
    # 第一个节点为根节点
    root = Node(int(input()))
    while True:
        try:
            # 从根节点开始插入
            root.insert(Node(int(input())))
        # 因为题目没有设置结束条件，所以如果acm那边停止输入了，这里抓取一个EOF异常来强行break
        except EOFError:
            break
        except Exception:
            break
    level_order(root)

```
---
### 5.2 检查二分查找树
[原题地址](https://acm.bsu.by/courses/246/problems/4558/)

#### 题意
根据输入的数据构成一棵树，然后检查这棵树是否为二分查找树。如果是，则输出YES，否则输出NO

输入：第一行n，代表这棵树有n个节点，从第二行开始到第1 + n行，则代表着不同的n个节点，
其中第一个数字代表该节点的值，第二个数字代表这个节点的父节点是第几个节点，第三个字母L代表是左子节点；R代表是右子节点

7 - 代表第一个节点，并且是根节点,值为7

    7

4 1 L - 代表第二个节点，值为4，是第一个节点7的左子节点

        7
    4

11 2 L - 代表第三个节点，值为11，并且是第二个节点4的左子节点

            7
        4
    11

5 1 R - 代表第四个节点，值为5，并且是第一个节点7的右子节点
            
            7
        4       5
    11

1 2 R - 代表第五个节点，值为1，并且是第2个节点4的右子节点
        
                7
        4               5
    11       1

9 4 L - 代表第六个节点，值为9，并且是第4个节点5的左子节点

                7
        4               5
    11       1       9

2 4 R - 代表第七个节点，值为2，并且是第四个节点5的右子节点
    
                7
        4               5
    11       1       9       2

很明显，这不是一个二分查找树，所以输出NO


#### 解析
每个位置的节点，都有个取值区间，用递归的方式，遍历每个子节点，并且压缩区间即可。

``` python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    #先不做判断，直接插入
    def insert_left(self, node):
        self.left = node
        
    #先不做判断，直接插入
    def insert_right(self, node):
        self.right = node

# 判断node是不是大于最小值，小于最大值，如果不是，就返回false，结束循环
# 如果是，那么再把左右子节点分别拿来判断
# 其中左节点的min_value不变，max_value变成了node.value；右节点的max_value不变，min_value变成了node.value，比如：
#              7
#         2         9
#      1    5     8    11
#          4 6
# 7 在（-2 ** 31, 2 ** 31）之间，所以判断2和9合不合法
# 2在7左边，所以要比7小，所以判断2是否在（-2 ** 31, 7）之间；9在7右边，比7大，所以要判断9是否在（9, 2 ** 31）之间
# 5在2的右边，所以要比2大，所以要判断5是否在（2, 7）之间，6在5的左边，所以要判断6是否在（2, 6）之间，一直递归到子节点为None，结束递归
def check_BST(node, min_value, max_value):
    if node is None:
        return True
    # 因为题目要求相等的值，可以在右边，所以这里用了 < min_value而不是 <= min_value
    if node.value >= max_value or node.value < min_value:
        return False
    return check_BST(node.left, min_value, node.value) and check_BST(node.right, node.value, max_value)


if __name__ == '__main__':
    num = int(input())
    root_value = int(input())
    root = Node(root_value)
    # 把所有节点都暂存在nodes数组里面
    nodes = [root]
    res = True
    for i in range(1, num):
        line = input().split()
        value = int(line[0])
        parent = int(line[1])
        direction = line[2]
        # 根据题意，父节点nodes数组中的第parent个节点，又因为数组是从0开始的，所以实际上要减一
        parent_node = nodes[parent - 1]
        node = Node(value)
        # 如果值小于父节点，并且是左边，那么就直接插入左边
        if value < parent_node.value and direction == 'L' and parent_node.left is None:
            parent_node.insert_left(node)
        # 如果值大于父节点，并且是右边，那么就直接插入右边
        elif value >= parent_node.value and direction == 'R' and parent_node.right is None:
            parent_node.insert_right(node)
        # 如果都不是，那证明该树肯定不是BST，所以直接返回False结束循环就行了
        else:
            res = False
            break
        nodes.append(node)
    if res:
        # 经过上面筛选，不代表这棵树就符合BST，只能证明每个左子节点都比父节点小；右子节点都比父节点大，但是可能还存在这种情况：
        #         5
        #      2     7
        #           1
        # 比如上面，1比7小，但是1也在5的右边，应该要比5大，所以这棵树也是不合法的，所以要进一步判断
        res = check_BST(root, -2 ** 31, 2 ** 31)
    if res:
        print('YES')
    else:
        print('No')

```
---
### 5.3 修复二分查找树
[原题地址](https://acm.bsu.by/courses/246/problems/4559/)

#### 题意
已知一颗二分查找树的形状，不可变；但是值可能对不上，求改变这棵树的值，最少需要多少步才能把这棵树修复成一个合法的二分查找树
输入：

3 - 代表接下来的树有3个节点

8 0 - 第一个节点，值为8，根节点

5 1R - 第二个节点，值为5，在第一个节点的右边

9 1L - 第三个节点，值为9，在第一个节点的左边基本上构建树的规则跟5.2一样

        8                       8
                    ->
    9       5               5       9
由此可见，需要变换两次，才能使这棵树合法，所以输出2

根据题目要求，此处还会继续输入n，如果n是0，结束；如果n不是0，则代表接下来还会输入一颗有n个节点的树，直到输入0为止

#### 解析
利用中序遍历一颗正常的树之后发现，输出的结果是一个递增的序列，所以反过来思考，将一颗损坏的树中序遍历出来的序列，改变成有序的序列，就可以修复这颗树了。

比如这棵损坏的树：

				8
		4				7
 	1		3		9		11

中序遍历的结果是：1 4 3 8 9 7 11，我们将其变成1 4 7 8 9 10 11即可修复这棵树了，即：

				8
		4				10
 	1		7		9		11
	
因此，这题就变成了，将无序的数组，变成有序的数组，最少需要修改几个数字。

把无序的数组，变成有序的数组之前，我们可以先找出最长递增子序列，这部分不用改；然后改变其他数字，让这些数字跟这个最长的递增子序列组合成一个新的有序数组即可。这样能保证要修改的数字是最少的。

比如上面的案例里面，最长的递增子序列是1 4 8 9 11，我们把3和7也改一下，就变成了1 4 7 8 9 10 11，这样只需要改变两次，即可让整个数组有序了。

但是，考虑到题目要求：树的节点都是正整数，因此，这题不止是求最长递增子序列，还要满足两个限定条件

1、如果数组是1、5、2、6、7，不难看出，最长递增子序列是1、2、6、7；但是在1和2之间，没有其余整数了，也就是说，第二个数字5，无论改成什么数字，都无法使这个数组变成有序数组，因此，最长递增子序列必须满足要求：当i大于j的时候，arr[i] >= arr[j] + ( i - j ),这样才能保证i和j之间能插入i - j 个数字；

2、如果数组是3 4 2 7 9，不难看出，最长递增子序列是2 7 9，但是2之前，需要插入两个比2小的数字，但是题目要求只能是正整数，所以只能插入一个1，无法插入更小的数字了，因此，最长递增子序列必须满足arr[i] > i,这样才能保证，在i前面，能至少插入i个数字
	

``` python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 中序遍历；考虑到该题最高可能有上三十万个节点，用递归可能会导致栈溢出，所以不用递归，用循环
def mid_order(node, lst):
    stack = []
    pos = node
    while pos is not None or len(stack) > 0:
        if pos is not None:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
	    # 将节点中序遍历存到lst里面去
            lst.append(pos.value)
            pos = pos.right

# 用动态规划（见7.2）的方法求出中序遍历结果的lst的最长递增子序列
def fix_arr(arr):
    max_len = 1
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
	    # arr[i] - arr[j] >= i - j：保证i和j之间至少能插入i-j个整数
	    # arr[i] >= i + 1 and arr[j] >= j + 1：保证第n个数字之前至少能插入n个整数
            if arr[j] < arr[i] and arr[i] - arr[j] >= i - j and arr[i] >= i + 1 and arr[j] >= j + 1:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])
    # 求出最长递增子序列的长度后，用数组长度减去该长度，就是至少要修改的节点的次数
    return len(arr) - max_len


if __name__ == '__main__':
    f = open("fix.out", "w")
    file = open("fix.in")
    i = int(file.readline())
    try:
        while i != 0:
            lst = []
            for j in range(i):
                line = file.readline().split()
                value = int(line[0])
                father = line[1]
                node = Node(value)
                if father != '0':
                    if father[-1] == 'L':
                        lst[int(father[:-1]) - 1].left = node
                    else:
                        lst[int(father[:-1]) - 1].right = node
                lst.append(node)
            arr = []
            mid_order(lst[0], arr)
            print(fix_arr(arr), file=f)
            i = int(file.readline())
    except EOFError:
        pass
    except Exception:
        pass
```
---

## 6. 计算二叉树

---

### 6.1 计算BST序列
[原题地址](https://acm.bsu.by/courses/246/problems/4564/)

#### 题意
根据题目5.1，我们可以通过输入一串数组生成一个BST，这题要求根据一个数组生成一个BST，
然后求能生成一个一模一样的BST的数组总共有多少种

比如输入 5 2 4 1 8 7，可以生成树：

                5
        2               8
    1       4       7

同理，输入 5 2 1 4 8 7、5 2 8 7 4 1、5 2 8 7 1 4、5 2 1 8 7 6等数组都可以生成这样一个一模一样的树
这种可以生成一模一样的树的情况，总共有20种，所以输出20即可
#### 解析

我们可以把一棵树，变成左右两颗子树，举个例子8 4 12 2 6 10 14 1 3 5 7 9 11 13可以组成下面的树：

                                    8
                    4                               12
            2               6               10                  14
        1        3       5              9        11       13          15

然后8只能排在数组的第一位，所以现在把8分成左右两棵子树分别是左边的4 2 6 1 3 5  和右边的12 10 14 9 11 13 15

我们先尝试算一下左边的子树可能存在多少种情况，把它也分成两棵树看看：2 1 3和6 5

2 1 3这棵树，2是根节点，不能动，所以存在C(2,1)= 2种情况，即2 1 3,2 3 1；同理右边则是C(1,1) 即 6 5，一种情况

所以在4 2 6 1 3 5  这种组合里面，总共存在C(5,3) * 2 * 1 = 20种情况

1和3互相顺序不重要，只要再2后面即可，可以等同，5也是，所以简化成4 2 6 a a b；

其中，a要在2后面；b要在2后面，变成排列组合问题；

首先不考虑2和a的顺序，即把2 a a 插入到6 b中，所以有A(5,5)/A(2,2)种可能；再除去a在2前面的情况，即A(3,2)

所以总共有A（5,5）/A(3,2)/A(2,2) = C(5,3) = 10种情况；然后再考虑到两颗子树的情况，乘以子树的数量，所以总共有C(5,3) * 2 * 1 = 20种情况

再往上的树以此类推即可。







``` python
from itertools import combinations


def sequences(nums):
    if not nums:
        return 1
    left = [i for i in nums if i < nums[0]]
    right = [i for i in nums if i > nums[0]]
    return len(list(combinations(nums[1:], len(left)))) * sequences(left) * sequences(right)


if __name__ == '__main__':
    print(sequences(list(map(int, input().split()))))

```
---
### 6.2 计算AVL树
[原题地址](https://acm.bsu.by/courses/246/problems/4565/)


#### 题意
[平衡二叉树](https://en.wikipedia.org/wiki/AVL_tree) 是指左右子树的高度差不超过1的二分查找树

要求输入数字n，输出拥有n个节点的平衡二叉树最多存在几种情况

比如拥有5个节点的平衡二叉树，拥有以下几种形态：

            4            3              3               4           4           3
        2      5    2       5       2       5      2       6    2       6    2      5
      1   3        1       4       1         6      3       5    3       7         4  6

共6种形态，所以输出6即可
#### 解析

这是一道递归题，节点为n，高度为h的树，左右子树也是二叉平衡树，可能为高度、节点分别为h-1,a及h-1,n-1-a;
或者分别为h-1,a;一个为h-2,n-1-a；
所以我们分别求出以上四种情况下的二叉平衡树，然后每种情况的二叉平衡树再分成两颗树

最后把这些都加起来就是所有的情况了

``` python
from math import log

n = int(input())
# 根据题目提示算出来的节点为n的树的高度范围
max_height = int(1.45 * log(n + 2, 2)) + 1
min_height = int(log(n + 1, 2))
# 这个数组代表avl[a][b]为节点为a、高度为b的情况下总共有多少种情况
avl_list = [[0 for i in range(max_height)] for j in range(n + 1)]
# 先求出0 1,1 0,0 0，1 1分别是多少，由于0 1,1 0是0，数组默认值是0，所以不用额外赋值了
avl_list[0][0] = 1
avl_list[1][1] = 1
# 从2个节点，高度为2开始循环
for i in range(2, n + 1):
    for j in range(2, max_height):
        for k in range(i):
            # 节点数为i，高度为j的二叉平衡树，在左右子树都相同的高度都相同的情况下，左右子树的节点和高度分别为
            # i - k - 1,j-1 和 k,j - 1,； 因为是for k in range(i)，以i为4为例，则左右子树的节点数在最内层的循环分别是
            # 3和0; 2和1; 1和2, 0和3，这四种情况下的所有情况数加起来，就是节点为4，左右子树相等的情况下的所有情况
            avl_list[i][j] = (avl_list[i][j] + avl_list[i - k - 1][j - 1] * avl_list[k][j - 1])
            # 节点数为i，高度为j的二叉平衡树，在左右子树高度不相同的情况下，左右子树的节点和高度分别是：
            # i - k -1,j-2 和 k, j - 1，所以跟上面情况一样，在内循环把所有的节点情况都加起来即可
            # 注意，这里乘以2了，以为左右子节点的高度不同分别存在左边为j-2，右边为j-1和左边为j-1右边为j-2的情况，所以要乘以2
            avl_list[i][j] = (avl_list[i][j] + 2 * avl_list[i - k - 1][j - 2] * avl_list[k][j - 1])


ans = 0
# 因为上面只是求出了节点为n高度为i的情况，而不是不限高度的所有情况
# 所以这里进行一次循环，从最小高度到最大高度，都加起来，才是最终的答案
for i in range(min_height, max_height):
    ans += avl_list[n][i]
print(ans)

```
---
## [线段树](https://b23.tv/uiWgcbz)

---
### 7.1 线段树
[原题地址](https://acm.bsu.by/courses/246/problems/4566/)

#### 题意
第一行输入n,m

接下来m行分别输入p k l r

代表有n个篮筐，分别编号从1到n，然后每次输入，都会把k个篮球扔到p号篮筐里面，需要输出从l号篮筐到r号篮筐，总共有几个篮球

打个比方

第一行输入3 3，有3个篮球，编号1,2,2，然后接下来3行输入分别输入：

1 3 1 2 - 在1号篮筐扔3个球，现在3个篮筐的篮球数分别是3 0 0，所以1到2号篮筐总共有3个篮球，输出3

2 5 2 3 - 在2号篮筐扔5个球，现在3个篮筐的篮球数分别是3 5 0，所以2到3号篮筐总共有5个篮球，输出5

3 4 1 3 - 在3号篮筐人4个球，现在3个篮筐的篮球数分别是3 5 4，所以1到3号篮筐总共有12个篮球，输出12


#### 解析
这题主要是运用线段树的区间求和功能，点[此处](https://b23.tv/uiWgcbz) 看视频应该就能搞定这题了，假设现在有9个球，生成的线段树如下：

                                    [1-9]
                    [1-5]                         [6-9]
            [1-3]           [4-5]           [6-7]     [8-9]
        [1-2]   [3,3]   [4,4]   [5,5]   [6,6] [7,7]  [8,8] [9,9]
    [1,1]   [2,2]

现在每个篮筐的篮球数都是0，所以如下：

                                      0
                                    [1-9]
                      0                             0
                    [1-5]                         [6-9]
              0               0               0         0
            [1-3]           [4-5]           [6-7]     [8-9]
          0       0       0       0       0     0      0     0 
        [1-2]   [3,3]   [4,4]   [5,5]   [6,6] [7,7]  [8,8] [9,9]
      0       0 
    [1,1]   [2,2]

假设我们现在往5号篮筐扔3个篮球，从根节点开始，5在区间1-9之间，所以[1-9]位置的篮球数变成3,
5在1-9区间的左边，所以左边的[1-5]的篮球数也变成了3,5在[1-5]的右边，所以[4-5]也变成了3,最终[5,5]也变成了3，线段树目前就变成了：

                                      3
                                    [1-9]
                      3                             0
                    [1-5]                         [6-9]
              0               3               0         0
            [1-3]           [4-5]           [6-7]     [8-9]
          0       0       0       3       0     0      0     0 
        [1-2]   [3,3]   [4,4]   [5,5]   [6,6] [7,7]  [8,8] [9,9]
      0       0 
    [1,1]   [2,2]

再往8号位置扔4个篮球，那么就变成了

                                      7
                                    [1-9]
                      3                             4
                    [1-5]                         [6-9]
              0               3               0         4
            [1-3]           [4-5]           [6-7]     [8-9]
          0       0       0       3       0     0      4     0 
        [1-2]   [3,3]   [4,4]   [5,5]   [6,6] [7,7]  [8,8] [9,9]
      0       0 
    [1,1]   [2,2]

再往2号位置扔2个篮球，就变成了

                                      9
                                    [1-9]
                      5                             4
                    [1-5]                         [6-9]
              2               3               0         4
            [1-3]           [4-5]           [6-7]     [8-9]
          2       0       0       3       0     0      4     0 
        [1-2]   [3,3]   [4,4]   [5,5]   [6,6] [7,7]  [8,8] [9,9]
      0       2 
    [1,1]   [2,2]

这时候如果我们要查询1-9总共有多少球，可以很明显的得出是9,1-5有多少个球则是5个；

但是如果要求2到8号位置有多少球呢？把2-8拆分成不同的区间即可：比如1-5包含了2；6-9包含了8，所以这两个区间都包含了一部分；

我们继续往下，1-3包含了一部分，4-5完全被2-8包含，所以没必要往下走了；同理，6-7完全被包含；8-9包含了一部分；

1-3往下，1-2包含了一部分，3,3完全被包含，8,8完全被包含，9,9完全不包含；然后1-2再往下，1,1完全不包含，2,2完全被包含

随意最终[2-8]总共有[2,2] + [3,3] + [4-5] + [6-7] + [8,8] = 2 + 0 + 3 + 0 + 4 = 9个篮球

以上就是线段树的构建和区间求和，考虑到如果篮筐数n如果比较大，构建线段树将会是个很耗时的情况，我们只需要像5.3一样，把这棵树存在数组里面即可，
其中a[i]的左子节点为a[2 * i + 1]，右子节点为a[2 * i + 2]，这样会省去构建线段树花费的时间,因为构建的时候只需要生成一堆0即可：

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

第一次扔3个篮球到5号位置，从根节点a[0]开始，分别把a[0],a[2 * 0 + 1 = 1],a[2 * 1 + 2 = 4],a[2 * 4 + 2 = 10]加3即可：

[3,3,0,0,3,0,0,0,0,0,3,0,0,0,0,0,0]

同理，接下来两次扔篮球：

[7,3,4,0,3,0,4,0,0,0,3,0,0,4,0,0,0]

[9,5,4,2,3,0,4,2,0,0,3,0,0,4,0,0,2]

而求[2-8]的篮球数，则是a[16] + a[8] + a[4] + a[5] + a[13]即可



``` python
class Tree:
    # 初始化线段树，因为存在数组里面，所以直接声明一堆0即可
    # 长度为n的数组，最长可以被分为 n + n / 2 + n / 4 + n / 8 + ..... + 2 + 1，即 4 * n - 1个节点
    def __init__(self, n):
        self.arr = [0] * ( 4 * n)
    
    # 投num个篮球到index位置的篮筐
    # index : 篮球的编号
    # pos : 线段树数组的位置
    # left : 左端点
    # right : 右端点
    # num : 篮球的数量
    def add(self, index, pos, left, right, num):
        # 当前位置加上num
        self.arr[pos] += num
        # 如果左端点和右端点相等，结束递归
        if left == right:
            return
        mid = (left + right) // 2
        # 如果篮球编号在左半边，那就add左节点即 2 * pos + 1位置的节点，否则add右节点，即2 * pos + 2位置的节点
        if index <= mid:
            self.add(index, 2 * pos + 1, left, mid, num)
        else:
            self.add(index, 2 * pos + 2, mid + 1, right, num)
    
    # 查询从l到r位置有多少个篮球
    # l,r ：要查询的篮球的左右子端点
    # pos ：当前节点在线段树数组中的位置
    # left,right ：当前节点的左右端点
    def query(self, l, r, pos, left, right):
        # 如果l,r完全包含了left,right，直接返回当前位置的篮球数
        if l <= left and r >= right:
            return self.arr[pos]
        mid = (left + right) // 2
        left_value = 0
        right_value = 0
        # 如果l在左边，那就查询l，r在左边有哪些地方有值
        if mid >= l:
            left_value = self.query(l, r, 2 * pos + 1, left, mid)
        # 如果r在右边，就查询l,r在右边在那些地方有值
        if mid < r:
            right_value = self.query(l, r, 2 * pos + 2, mid + 1, right)
        # 然后把左右两边的值加起来
        return left_value + right_value
        
        # 按上面的例子[9,5,4,2,3,0,4,2,0,0,3,0,0,4,0,0,2] ，查询[2-8]  
        # 从根节点0进来，left是1，right是9
        # 所以left = query(2, 8,  1, 1, 5), right = query(2, 8,  2, 6, 9)
        # query(2, 8,  1, 1, 5) : left =  query(2, 8,  3, 1, 3),right = query(2, 8,  4, 4, 5),其中4-5被2-8包含，所以right是arr[4]=3
        # query(2, 8,  3, 1, 3) : left = query(2, 8,  7, 1, 2),right = query(2, 8,  8, 3, 3),其中3,3被2-8包含，所以right是arr[8]=0
        # query(2, 8,  7, 1, 2) : mid < l，所以left=0;right = query(2, 8,  16, 2, 2) = a[16] = 2
        # 所以 query(2, 8,  1, 1, 5) = a[16] + a[8] + a[4] = 5
        # 同理可求query(2, 8,  2, 6, 9) = a[5] + a[13] = 4
        # 最终等于9


if __name__ == '__main__':
    baskets, num = map(int, input().split())
    tree = Tree(baskets - 1)
    for i in range(num):
        p, k, l, r = map(int, input().split())
        # 因为篮球的编号是从1~baskets，而数组的编号是从0到baskets-1，所以下面只要是跟编号有关的(l,r,baskets)，都减一
        tree.add(p - 1, 0, 0, baskets - 1, k)
        print(tree.query(l - 1, r - 1, 0, 0, baskets - 1))

```
---
### 7.2 最长递增子序列
[原题地址](https://acm.bsu.by/courses/246/problems/4567/)

#### 题意
第一行输入n，第二行输入n个数字

输出n个数字组成的数组的最长递增子序列的长度是多少

比如数组为4 7 6 5 8 2 9 1 10，那么最长的递增子序列是4 6 8 9 10，所以输出5

#### 解析
**尚未解决**

``` python
# 尚未解决

```
