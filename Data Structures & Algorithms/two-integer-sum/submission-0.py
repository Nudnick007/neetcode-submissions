class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i,n in enumerate(nums):
            temp = target - n
            if temp in d:
                return [d[temp],i]
            d[n] = i