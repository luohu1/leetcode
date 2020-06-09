#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, element in enumerate(nums):
            hash_map[element] = idx
        for idx_x, x in enumerate(nums):
            y = target - x
            if y not in hash_map:
                continue
            idx_y = hash_map.get(y)
            if idx_x == idx_y:
                continue
            return [idx_x, idx_y]


# @lc code=end
