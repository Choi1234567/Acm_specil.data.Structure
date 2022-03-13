def merge(arr1, arr2):#i 是arr1的下标，index代表arr2的下标，2插入1
    ans = arr1.copy()
    index = 0
    for i in range(0, len(arr2)):
        while index < len(arr1):
            if arr2[i] <= arr1[index]:
                ans.insert(index + i, arr2[i])#i代表a原来第i个位置，index代表之前以及插入了几个数字，所以是i+index
                break#while 这层中止
            else:
                index += 1
        else:
            ans = ans + arr2[i:]#例子输入都是已经排完序的，默认最后一个最大，所以把剩余的插入即可
            break
    return ans


if __name__ == "__main__":
    input()
    arr1 = list(map(int, input().split()))
    input()
    arr2 = list(map(int, input().split()))
    c = merge(arr1, arr2)
    print(" ".join(map(str, c)))#把数组里面的字符串，用空格连起来，与split相反