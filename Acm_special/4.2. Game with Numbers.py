def process(lst, l):
    count = 0
    min_num = min(lst)
    max_num = max(lst)
    if max_num == min_num:
        return 0
    while True:
        if min_num == 1:
            for i in lst:
                count += i - 1
            return count
        max_num = 0
        max_position = 0
        for i in range(0, l):
            num = lst[i]
            if num != min_num and num // min_num > 1:
                c = num // min_num - 1
                count += c
                num = num - c * min_num
                lst[i] = num
            if max_num <= min_num + num % min_num:
                max_position = i
                max_num = num
        if max_num == min_num:
            return count
        lst[max_position] = max_num - min_num
        count += 1
        min_position = max_position
        min_num = lst[min_position]


if __name__ == '__main__':
    l = int(input())
    lst = list(map(int, input().split()))
    print(process(lst, l))