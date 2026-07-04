class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        e1 = m - 1
        e2 = n - 1
        last = m + n -1
        while e1 >= 0 and e2 >= 0:
            if nums1[e1] >= nums2[e2]:
                nums1[last] = nums1[e1]
                e1 -=1
            else:
                nums1[last] = nums2[e2]
                e2 -=1
            last -=1
        print(nums1)
        print(e1,e2)
        while e2 >= 0:
            nums1[last] = nums2[e2]
            e2 -=1
            last -=1
        while e1 >= 0:
            nums1[last] = nums1[e1]
            e1 -=1
            last -=1
        
