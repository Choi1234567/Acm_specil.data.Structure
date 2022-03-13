def add(idx, val, n, t):
    idx += n
    t[idx] = val
    while idx:
        l = idx
        r = idx
        if idx & 1:
            l -= 1
        else:
            r += 1
        t[idx // 2] = max(t[l], t[r])
        idx //= 2


def ask(l, r, n, t):
    res = 0
    l += n
    r += n
    while l <= r:
        if l % 2 == 1:
            res = max(t[l], res)
            l += 1
        if r % 2 == 0:
            res = max(t[r], res)
            r -= 1
        l //= 2
        r //= 2
    return res


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    tree = [0] * 4 * n
    s = sorted(set(nums))

    cnt = 1
    m = {}
    for i in s:
        m[i] = cnt
        cnt += 1
    res = 0
    for i in range(n):
        v = ask(1, m[nums[i]] - 1, n, tree)
        res = max(res, v + 1)
        add(m[nums[i]], v + 1, n, tree)

    print(res)