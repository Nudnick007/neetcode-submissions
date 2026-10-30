from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    new = []
    k = len(arr)
    while k:
        new.append(arr.pop())
        k -=1
    return new


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
