if __name__ == "__main__":
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