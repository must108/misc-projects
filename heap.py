
import heapq

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
heapq.heapify(A)
# heap sort... my beloved

heapq.heappush(A, 4)
a = heapq.heappop(A)
print(a) # will print the smallest value

def heapsort(arr):
    heapq.heapify(arr)
    return arr

B = [-5, 16, -24, 10, 15, 4, 5, 3, 2, 9, 8, 1]
B = heapsort(B)
print(B) # heapsort. O(1) space, O(nlgn) time

b = heapq.heappushpop(B, 99)
print(b) # still the smallest val

# access min:
print(B[0]) # should be negative 5, given the array above does not change

# max heap... 

C = [36, 27, 15, -15, -25, -16, 4, 1, 2, -1, -5, 5, 6]

for i in range(len(C)):
    C[i] = -C[i] # inverse all values in the heap

heapq.heapify(C)
print(C)

largest = -heapq.heappop(C)
print(largest)

heapq.heappush(C, -7) # to insert regular value 7

tup = [('c', 3), ('a', 1), ('b', 2)]

heapq.heapify(tup)
print(heapq.heappop(tup))
print(heapq.heappop(tup))
print(heapq.heappop(tup))

# yay

