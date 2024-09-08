
def main():
    arr = [0, 1, 2, 3, 4, 5]
    pre = [0] * len(arr)

    for i in range(len(arr)):
        if i == 0:
            pre[i] = arr[i]
        else:
            pre[i] = arr[i] + pre[i-1]

    print(pre)


if __name__ == "__main__":
    main()
