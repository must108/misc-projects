import bisect

arr = [1, 3, 8, 2, 9, 2, 5, 6]
arr.sort()
print(arr)

print(bisect.bisect_left(arr, 8))
print(bisect.bisect_right(arr, 8))

bisect.insort_left(arr, 8)
bisect.insort_right(arr, 8)

print(arr)