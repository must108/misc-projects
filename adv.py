import heapq
from collections import deque, defaultdict, Counter
from enum import Enum

arr = [1, 5, 5, 3, 1, 2, 7, 6, 8, 9, 10, 5, 4] # frequency list ez

print(Counter(arr))

h = defaultdict() # hashmap...

for num in arr:
    h[num] = 1 + h.get(num, 0)

print(h)

arr2 = arr.copy()

heapq.heapify(arr2)

for num in arr2:
    print(num, end=" ")

q = deque()
q.append(1)
q.append(2)
print(q)
q.popleft()
print(q)

h1 = set() # no key : value like in hashmap. just key basically. O(1) time

strarr = [
    "hello", "goodbye"
]

for i, j in enumerate(strarr):
    print(i, j)

# enums... type safety and elimination of magic values

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
# if something depended on these numbers, now its easy!

print(Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW)
print(Color.RED.name, Color.GREEN.name, Color.BLUE.name, Color.YELLOW.name)
print(Color.RED.value, Color.GREEN.value, Color.BLUE.value, Color.YELLOW.value)
# pretty chill...
