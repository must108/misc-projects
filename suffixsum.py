
def main():
    arr = [0, 1, 2, 3, 4, 5]
    n = len(arr)
    pre = [0] * n

    for i in range(n-1, 0, -1):
        if i == n-1:
            pre[i] = arr[i]
        else:
            pre[i] = arr[i] + pre[i+1]

    print(pre)


if __name__ == "__main__":
    main()
