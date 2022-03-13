if __name__ == '__main__':
    length, num = map(int, input().split())#num就是1到num这个区间
    price = total_price = stack = lift = right = 0#price临时价格，total-price总价格，stack，存着1到n出现的次数,stack[i]代表i在left和right区间里出现的次数
    arr_sign = [0] * (num + 1)#arr_sign是记录当前左右指针的区间内，已经包含了1到k的哪些数字
    arr = list(map(int, input().split()))
    while lift < length - num + 1:#包含所有数字了，就移动左；不包含所有数字了，就移动右
        if right < length and stack < num:#每次移动，如果发现数字是1~k的，就记录到arr_sign里面去，一旦发现arr_sign包含1~4的所有数字的时候，第一个total_price就出来了
            if arr[right] <= num and arr_sign[arr[right]] == 0:#一旦stack = num的时候，就证明当前区间已经包含1~num的所有数字了
                stack += 1#stack代表当前区间已经有几个1~k的数字了，stack小于num，就移动右指针，然后一直到stack包含所有元素，然后移动左指针
                arr_sign[arr[right]] += 1
            elif arr[right] <= num and arr_sign[arr[right]] > 0:#如果arr_sign[1]等于1的话，证明1已经出现过了，所以stack就不重复加一次了
                arr_sign[arr[right]] += 1
            price += arr[right]
            right += 1
        elif right >= length and stack < num:
            break
        else:
            if price < total_price or total_price == 0:#比较价格，每次包含所有元素了，就会对比一下当前价格price和总价格totalprice
                total_price = price
            if arr[lift] <= num and arr_sign[arr[lift]] == 1:
                stack -= 1
                arr_sign[arr[lift]] -= 1
            elif arr[lift] <= num and arr_sign[arr[lift]] > 1:
                arr_sign[arr[lift]] -= 1
            price -= arr[lift]
            lift += 1

    print(total_price)
          #Temporary Price