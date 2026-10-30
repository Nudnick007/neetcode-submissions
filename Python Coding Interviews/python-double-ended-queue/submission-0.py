from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    d_queue = deque(arr)
    while k:
        d_queue.appendleft(d_queue.pop())
        k -=1
    return d_queue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
