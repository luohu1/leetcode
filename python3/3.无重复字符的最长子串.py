#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == len(set(s)):
            return len(s)

        for length in range(len(set(s)), 0, -1):
            for p1 in range(len(s) - length + 1):
                p2 = p1 + length
                if len(s[p1:p2]) == len(set(s[p1:p2])):
                    return length


# @lc code=end
