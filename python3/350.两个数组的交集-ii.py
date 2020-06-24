#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#


# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not (nums1 and nums2):
            return []

        arr = {}
        for n in nums1:
            arr.setdefault(n, [0, 0])
            arr[n][0] += 1

        for n in nums2:
            arr.setdefault(n, [0, 0])
            arr[n][1] += 1

        ret = []
        for k, v in arr.items():
            if min(v) != 0:
                ret.extend([k] * min(v))

        return ret


# @lc code=end
