from typing import List


def disallow_negatives(num: int) -> int:
    if num < 0:
        return 0
    return num


def max_difference(nums: List[int]) -> int:
    mx = 0
    first = nums[0]
    for i in range(1,len(nums)):
        mx = max(mx,nums[i] - first)
        first = nums[i]
    return mx



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
