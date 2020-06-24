#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not (nums1 and nums2):
            return []

        arr = dict.fromkeys(set(nums1), 0)
        for n in nums2:
            if n in arr:
                arr[n] += 1
        ret = []
        for k, v in arr.items():
            if v != 0:
                ret.append(k)
        return ret


# @lc code=end
