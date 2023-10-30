class Solution:

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        pass

    def findMedianSortedArrays2(self, nums1: list[int], nums2: list[int]) -> float:
        count1 = 0
        for i in nums1:
            count1+=i
        count2 = 0
        for i in nums2:
            count2+=i
        count = count1 + count2
        c = count/(len(nums1)+len(nums2))
        return c